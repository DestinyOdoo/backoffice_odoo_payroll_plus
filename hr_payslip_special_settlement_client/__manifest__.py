# -*- coding: utf-8 -*-
{
    'name': 'Payslip Settlement Client',
    'version': '17.0.1.0.0',
    'summary': 'Cliente para liquidaciones especiales de nómina',
    'description': '''
        Payslip Settlement Client
        =========================
        Módulo cliente que consume las APIs del servidor de liquidaciones especiales.
        
        **IMPORTANTE:** Este módulo requiere licencia válida de BackOffice.
        
        Características:
        * Validación de licencia contra servidor BackOffice
        * Consumo de APIs protegidas
        * Interfaz de usuario para liquidaciones
    ''',
    'sequence': 15,
    'category': 'Human Resources',
    'author': 'BACKOFFICE S.A.S.',
    'maintainer': 'BackOffice',
    'company': 'BackOffice S.A.S.',
    'website': 'https://www.boffice.cloud/',
    'depends': [
        'hr_payroll',
        'hr_novelty_client',
        'bo_license_client',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/type_settlement_view.xml',
        'views/assign_month_view.xml',
        'views/inherited_hr_payslip_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
