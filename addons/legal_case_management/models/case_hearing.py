# -*- coding: utf-8 -*-

from odoo import models, fields

class LegalHearing(models.Model):
    _name = 'legal.hearing'
    _description = 'Legal Hearing'

    name = fields.Char(string='Hearing Subject', required=True)
    
    case_id = fields.Many2one(
        'legal.case',
        string='Associated Case',
        required=True,
        ondelete='cascade')
        
    date_start = fields.Datetime(string='Start Date', required=True)
    location = fields.Char(string='Location')