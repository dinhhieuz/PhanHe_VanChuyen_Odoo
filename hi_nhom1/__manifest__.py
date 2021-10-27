# -*- coding: utf-8 -*-
{
    'name': "SHIPPER",
    'summary': """
        NHOM1""",
    'description': """
        Đây là module vận chuyển của nhóm 1
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -150,
    # any module necessary for this one to work correctly
    'depends': ['base','stock'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/module_nhom1.xml',
        'views/dang.xml',
        'views/cho.xml',
        'views/ds_shipper.xml',
        'views/ds_phieu.xml',
        'views/phieu_no.xml',
        'views/phieu_yes.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}