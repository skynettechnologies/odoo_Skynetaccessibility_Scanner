# -*- coding: utf-8 -*-
{
    'name': 'SkynetAccessibility Scanner',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Scan, monitor, and identify website accessibility issues across WCAG 2.0, 2.1, 2.2, ADA, Section 508, EN 301 549, UK Equality Act, Australian DDA, and Canada ACA. Get simple issue highlights with recommended fixes.',
    'author': 'Skynet Technologies',
    'website': 'https://www.skynettechnologies.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'models/skynet_scanner_model.xml',
        'security/ir.model.access.csv',      
        'views/skynet_scanner_views.xml',    
        'views/skynet_scanner_menu.xml',     
    ],
    'images': ['/static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
