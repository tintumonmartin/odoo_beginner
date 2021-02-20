# -*- coding: utf-8 -*-
{
    'name': "Interior - Website",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'website',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'static/src/xml/website_sale.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
