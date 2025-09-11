from odoo import models, fields, api, _
from odoo.exceptions import UserError

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Case Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    client_id = fields.Many2one('res.partner', string='Client', required=True, domain="[('is_client', '=', True)]")
    responsible_lawyer_id = fields.Many2one('res.partner', string='Responsible Lawyer', required=True, domain="[('is_lawyer', '=', True)]")
    open_date = fields.Date(string='Open Date', default=fields.Date.context_today)
    close_date = fields.Date(string='Close Date')
    stage = fields.Selection([
        ('intake', 'Intake'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    ], string='Stage', default='intake', tracking=True)
    description = fields.Text(string='Description')

    # --- NEW FIELDS AND METHODS START HERE ---

    fixed_fee_amount = fields.Monetary(string="Fixed Fee Amount", currency_field='company_currency_id')
    company_currency_id = fields.Many2one('res.currency', string='Company Currency', related='company_id.currency_id', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    
    invoice_count = fields.Integer(string="Invoice Count", compute='_compute_invoice_count')
    hearing_count = fields.Integer(string="Hearing Count", compute='_compute_hearing_count')

    def _compute_invoice_count(self):
        for case in self:
            case.invoice_count = self.env['account.move'].search_count([('invoice_origin', '=', case.name)])

    def _compute_hearing_count(self):
        for case in self:
            case.hearing_count = self.env['legal.hearing'].search_count([('case_id', '=', case.id)])
            
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('legal.case.sequence') or _('New')
        return super(LegalCase, self).create(vals)

    def write(self, vals):
        if 'stage' in vals and vals['stage'] == 'closed':
            vals['close_date'] = fields.Date.context_today(self)
        return super(LegalCase, self).write(vals)

    # Method for the "Create Invoice" button
    def action_create_invoice(self):
        self.ensure_one()
        if not self.fixed_fee_amount or self.fixed_fee_amount <= 0:
            raise UserError(_("Please set a fixed fee amount before creating an invoice."))

        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.client_id.id,
            'invoice_origin': self.name,
            'invoice_line_ids': [
                (0, 0, {
                    'name': f'Legal Services for Case: {self.name}',
                    'quantity': 1,
                    'price_unit': self.fixed_fee_amount,
                })
            ],
        }
        self.env['account.move'].create(invoice_vals)

    # Method for the "Invoices" smart button
    def action_view_invoices(self):
        return {
            'name': _('Invoices'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('invoice_origin', '=', self.name)],
        }

    # Method for the "Hearings" smart button
    def action_view_hearings(self):
        return {
            'name': _('Hearings'),
            'type': 'ir.actions.act_window',
            'res_model': 'legal.hearing',
            'view_mode': 'tree,form',
            'domain': [('case_id', '=', self.id)],
            'context': {'default_case_id': self.id}
        }

