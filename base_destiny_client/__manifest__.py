# -*- coding: utf-8 -*-
{
    'name': 'Base BackOffice Client',
    'summary': 'Cliente de configuraciones básicas BackOffice',
    'version': '17.0.1.0.0',
    'category': 'base',
    'website': 'https://www.boffice.cloud/',
    'author': 'BACKOFFICE S.A.S.',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'base_address_extended',
        'hr',
        'bo_license_client',
    ],
    'data': [
        'views/res_city_view.xml',
        'views/inherited_res_users.xml',
        'security/groups.xml',
    ],
    'license': 'LGPL-3',
}
