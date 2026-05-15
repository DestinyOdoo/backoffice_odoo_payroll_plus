# -*- coding: utf-8 -*-
{
    'name': 'Partner BackOffice Client',
    'summary': 'Cliente de campos adicionales para partners',
    'version': '17.0.1.0.0',
    'category': 'Base',
    'website': 'https://www.boffice.cloud/',
    'author': 'BACKOFFICE S.A.S.',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'bo_license_client',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'license': 'LGPL-3',
}
