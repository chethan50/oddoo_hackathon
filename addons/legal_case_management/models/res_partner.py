# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_lawyer = fields.Boolean(string="Is a Lawyer")
    is_client = fields.Boolean(string="Is a Client")