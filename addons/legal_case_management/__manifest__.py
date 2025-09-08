# -*- coding: utf-8 -*-
{
    'name': "Legal Case Management",

    'summary': """
        Manage legal cases, hearings, clients, and lawyers.""",

    'description': """
        A comprehensive module for legal firms to manage their cases,
        track hearings, and handle client and lawyer information efficiently.
    """,

    'author': "Your Hackathon Team",
    'website': "https://www.yourteam.com",

    'category': 'Services/Legal',
    'version': '1.0',

    'depends': ['base', 'mail', 'account', 'calendar'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    
    'application': True,
    'installable': True,
}