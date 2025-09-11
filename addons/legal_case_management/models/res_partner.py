from odoo import fields, models

class ResPartner(models.Model):
    """Extends the Partner model to add legal-specific flags."""
    _inherit = 'res.partner'

    is_lawyer = fields.Boolean(string="Is a Lawyer")
    is_client = fields.Boolean(string="Is a Client")