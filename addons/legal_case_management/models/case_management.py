from odoo import models, fields, api
from odoo.exceptions import UserError

class LegalCase(models.Model):
    _name = 'case.management'
    _description = 'Legal Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Case Name', required=True, tracking=True)
    reference = fields.Char(string='Reference', readonly=True, copy=False)

    client_id = fields.Many2one(
        'res.partner', string='Client', required=True,
        domain="[(\'is_client\', '=', True)]", tracking=True)

    responsible_lawyer_id = fields.Many2one(
        'res.partner', string='Responsible Lawyer', required=True,
        domain="[(\'is_lawyer\', '=', True)]", tracking=True)

    responsible_user_id = fields.Many2one('res.users', string='Responsible User', tracking=True,
                                          help='User responsible for the case (used in record rules)')

    case_type = fields.Selection([
        ('civil', 'Civil Litigation'),
        ('criminal', 'Criminal Defense'),
        ('corporate', 'Corporate Law'),
        ('family', 'Family Law'),
        ('ip', 'Intellectual Property')],
        string='Case Type', default='civil', tracking=True)

    stage = fields.Selection([
        ('intake', 'Intake'),
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled')],
        string='Stage', default='intake', tracking=True)

    close_date = fields.Date(string='Close Date', readonly=True, copy=False)

    case_hearing_ids = fields.One2many('case.hearing', 'case_id', string='Hearings')

    invoice_ids = fields.One2many('account.move', 'case_id', string='Invoices')

    attachment_count = fields.Integer(string='Attachments', compute='_compute_attachment_count')

    user_ids = fields.Many2many('res.users', 'case_user_rel', 'case_id', 'user_id', string='Case Members')

    @api.model
    def create(self, vals):
        # assign a sequence reference
        if not vals.get('reference'):
            seq = self.env['ir.sequence'].next_by_code('case.management')
            vals['reference'] = seq
        rec = super().create(vals)
        return rec

    @api.onchange('stage')
    def _onchange_stage_set_close_date(self):
        for rec in self:
            if rec.stage == 'closed' and not rec.close_date:
                rec.close_date = fields.Date.context_today(rec)

    def _compute_attachment_count(self):
        Attachment = self.env['ir.attachment']
        for rec in self:
            rec.attachment_count = Attachment.search_count([
                ('res_model', '=', 'case.management'), ('res_id', '=', rec.id)
            ])

    def action_open_attachments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attachments',
            'res_model': 'ir.attachment',
            'view_mode': 'tree,form',
            'domain': [('res_model', '=', 'case.management'), ('res_id', '=', self.id)],
        }

    def action_view_invoices(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('case_id', '=', self.id)],
        }

    def action_create_invoice(self):
        self.ensure_one()
        if not self.client_id:
            raise UserError('Please set a client on the case before creating an invoice.')

        # Try to get a product defined by the module (if you added demo data), else search by name.
        product = self.env.ref('legal_case_management.product_legal_services', raise_if_not_found=False)
        if not product:
            product = self.env['product.product'].search([('name', '=', 'Legal Services')], limit=1)
        if not product:
            # create a simple service product if none exists
            product_vals = {
                'name': 'Legal Services',
                'type': 'service',
            }
            product = self.env['product.product'].create(product_vals)

        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.client_id.id,
            'invoice_origin': self.reference or self.name,
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'quantity': 1.0,
                'price_unit': product.lst_price if product.lst_price else 0.0,
            })],
            'case_id': self.id,
        }
        invoice = self.env['account.move'].create(invoice_vals)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': invoice.id,
        }