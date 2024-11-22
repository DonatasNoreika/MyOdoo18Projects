# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'DN modulis',
    'version': '0.1',
    'category': 'Sales/Sales',
    'summary': 'DN modulis',
    'description': """
Donato Noreikos supermodulis.
For Odoo 18
    """,
    'depends': ['base', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/dn_project_view.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'license': 'LGPL-3',
}
