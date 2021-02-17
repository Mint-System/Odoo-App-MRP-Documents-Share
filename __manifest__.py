# -*- coding: utf-8 -*-
{
    'name': "MRP Documents Share",

    'summary': """
        Share product drawing and step files.
    """,

    'description': """
        Share product drawing and step files with vendors and show them during product assembling.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Uncategorized', # See odoo/addons/base/data/ir_module_category_data.xml
    'version': '14.0.1.0.0',

    'depends': ['mrp', 'purchase'],

    'data': [
        'views/ir_actions_act_window.xml',
        'views/ir_model_fields.xml',
        'views/ir_ui_menu.xml',
        'views/ir_ui_view.xml',
    ],

    'installable': True,
    'application': False,
}