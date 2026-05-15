# -*- coding: utf-8 -*-
{
    'name': 'HR Contract Completion Client',
    'version': '17.0.1.0.0',
    'author': 'BACKOFFICE S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'category': 'Human Resources',
    'summary': 'Cliente de terminación de contratos',
    'depends': [
        'base',
        'mail',
        'hr_payroll',
        'hr',
        'hr_novelty_client',
        'bo_license_client',
    ],
    'data': [
        'data/hr_contract_completion_data.xml',
        'views/hr_contract_completion_view.xml',
        'views/payslip_view.xml',
        'views/inherited_hr_novelty_view.xml',
        'views/inherited_hr_contract_view.xml',
        'wizard/contract_completion_reverse_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
