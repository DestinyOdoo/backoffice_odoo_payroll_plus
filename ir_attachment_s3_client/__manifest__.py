# -*- coding: utf-8 -*-
{
    'name': 'S3 Attachment Storage Client',
    'version': '17.0.1.0.0',
    'summary': 'Cliente para almacenamiento de adjuntos en S3',
    'category': 'Tools',
    'application': False,
    'author': 'BACKOFFICE S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'depends': [
        'base_setup',
        'hr',
        'bo_license_client',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/res_partner_view.xml',
    ],
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
}
