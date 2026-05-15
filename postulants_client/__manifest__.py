# -*- coding: utf-8 -*-
{
    'name': 'Postulants Client',
    'version': '17.0.1.0.0',
    'summary': 'Cliente de Postulantes',
    'category': 'Human Resources',
    'author': 'BACKOFFICE S.A.S.',
    'maintainer': 'BackOffice',
    'company': 'BackOffice S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'external_dependencies': {
        'python': ['mechanize', 'oauth2']
    },
    'depends': [
        'hr_recruitment',
        'hr_curriculum_vitae_client',
        'contacts',
        'bo_license_client',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_res_partner_view.xml',
        'views/inherited_hr_applicant_view.xml',
        'views/hr_referred_channel.xml',
        'views/inherited_hr_job.xml',
        'views/inherited_hr_cv_employee_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
