# -*- coding: utf-8 -*-
{
    'name': "Odoo Legal Management",
    'version': '1.0',
    'summary': "A comprehensive solution for managing legal cases and hearings.",
    'description': """
        A module to manage legal cases, clients, lawyers, and hearings within Odoo.
    """,
    'author': "Your Team Name",
    'website': "https://www.your-website.com",
    'category': 'Services/Legal',
    'depends': ['base', 'mail', 'calendar'],  # Added 'calendar'
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/res_partner_views.xml',
        'views/legal_case_views.xml',
        'views/legal_hearing_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
