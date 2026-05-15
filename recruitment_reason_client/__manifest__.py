# -*- coding: utf-8 -*-
{
    'name': 'Recruitment Reasons Client',
    'version': '17.0.1.0.0',
    'summary': 'Cliente de razones de reclutamiento',
    'category': 'Human Resources',
    'author': 'BACKOFFICE S.A.S.',
    'license': 'LGPL-3',
    'maintainer': 'BackOffice',
    'company': 'BackOffice S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'depends': [
        'hr_recruitment',
        'bo_license_client',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/recruitment_reason_view.xml',
        'views/inherited_recruitment_reason_view.xml',
        'views/job_position_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
