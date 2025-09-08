# -*- coding: utf-8 -*-

from odoo import models, fields

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Case Name', required=True, tracking=True)
    
    client_id = fields.Many2one(
        'res.partner',
        string='Client',
        required=True,
        domain="[('is_client', '=', True)]",
        tracking=True)
    
    responsible_lawyer_id = fields.Many2one(
        'res.partner',
        string='Responsible Lawyer',
        required=True,
        domain="[('is_lawyer', '=', True)]",
        tracking=True)
        
    case_type = fields.Selection([
        ('civil', 'Civil Litigation'),
        ('criminal', 'Criminal Defense'),
        ('corporate', 'Corporate Law'),
        ('family', 'Family Law'),
        ('ip', 'Intellectual Property')],
        string='Case Type',
        default='civil',
        tracking=True)
        
    stage = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled')],
        string='Stage',
        default='new',
        tracking=True)