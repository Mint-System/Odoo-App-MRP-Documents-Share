# -*- coding: utf-8 -*-
{
    'name': "MRP Documents Share",

    'summary': """
        Share product drawing and step files.
    """,

    'description': """
        Share product drawing and step files with vendors and link them in the workorder tablet view.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Manufacturing',
    'version': '14.0.1.2.0',

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