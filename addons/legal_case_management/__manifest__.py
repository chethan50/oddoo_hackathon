# -*- coding: utf-8 -*-
{
    'name': "Legal Case Management",
    'summary': "Manage legal cases, clients, lawyers, and hearings.",
    'description': """
        A minimal application to manage legal cases for law firms.
    """,
    'author': "Your Name",
    'website': "https://www.yourcompany.com",
    'category': 'Services/Legal',
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded in this specific order
    'data': [
        # 1. Security groups and rules must be loaded first.
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # 2. Data files (like sequences).
        'data/sequence_data.xml',
        
        # 3. Views (the user interface).
        'views/res_partner_views.xml', # This was missing, so I've added it.
        'views/legal_case_views.xml',
        'views/legal_hearing_views.xml', # This was missing, so I've added it.
        'views/menus.xml',
    ],
    'application': True,
}
