# -*- coding: utf-8 -*-
{
    'name': 'Bridges Custom Module',
    'summary': 'Contains company specific customizatons',
    'version': '1.0',
    'category': 'Tools',
    'description': """
KE Instruments Custom Module
===========================================================

Contains company specific customizations and configuration data

    """,
    'author': 'eXcec Business Consulting Ltd.',
    'depends': ['account','sale','purchase'],
    'website': 'http://www.excecbc.com',
    'data': [
        'config.xml',
        #'report_paperformat.xml',
        # 'layouts.xml', # have to do again for 11
        'views.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'images':[],
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
