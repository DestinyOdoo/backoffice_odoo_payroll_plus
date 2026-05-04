# -*- coding: utf-8 -*-
{
    'name': 'Certificado Laboral Client',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Cliente de certificado laboral',
    'description': """
        Certificado Laboral Client
        ==========================
        Módulo cliente con validación de licencia.
    """,
    'author': 'BACKOFFICE S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'depends': [
        'portal',
        'website',
        'hr',
        'hr_contract',
        'hr_destiny_client',
        'bo_license_client',
    ],
    'data': [
        'security/hr_employment_certificate_security.xml',
        'security/ir.model.access.csv',
        'report/employment_certificate_report.xml',
        'views/res_company_views.xml',
        'views/employment_certificate_views.xml',
        'views/portal_templates.xml',
        'views/website_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
