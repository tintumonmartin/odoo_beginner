# -*- coding: utf-8 -*-
{
    'name': "Railway Reservation",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
        Tony - user module
        Akilan - passenger module
        Varada- train module
        Madhu - station and ticket module
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/railway_management_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
