# -*- coding: utf-8 -*-
{
    'name': 'HR BackOffice Client',
    'summary': 'Cliente de HR Employee BackOffice',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'website': 'https://www.boffice.cloud/',
    'author': 'BACKOFFICE S.A.S.',
    'application': False,
    'installable': True,
    'depends': [
        'base_address_extended',
        'hr_payroll_destiny_client',
        'l10n_co',
        'bo_license_client',
    ],
    'data': [
        'views/hr_view.xml',
        'views/hr_contract_view.xml',
        'views/hr_contract_batch_view.xml',
        'views/inherited_partner_view.xml',
        'views/inherited_company_view.xml',
        'views/res_company_view.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
    ],
    'license': 'LGPL-3',
}
