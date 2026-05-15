# -*- coding: utf-8 -*-
{
    'name': 'HR Contract Report Client',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'author': 'BACKOFFICE S.A.S.',
    'maintainer': 'BackOffice',
    'company': 'BackOffice S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'depends': [
        'hr_contract',
        'hr_recruitment',
        'bo_license_client',
    ],
    'data': [
        'views/contract_section_views.xml',
        'views/contract_format_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
