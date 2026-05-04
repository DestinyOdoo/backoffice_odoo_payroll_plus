# -*- coding: utf-8 -*-
{
    'name': 'Portal de Novedades Client',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Time Off',
    'summary': 'Cliente del portal de novedades con validación de licencia',
    'description': """
        Portal de Novedades Client
        ==========================
        Módulo cliente con validación de licencia.
    """,
    'author': 'BACKOFFICE S.A.S.',
    'depends': [
        'portal',
        'hr_novelty_client',
        'website',
        'bo_license_client',
    ],
    'data': [
        'security/hr_novelty_portal_security.xml',
        'security/ir.model.access.csv',
        'views/hr_novelty_event_group_views.xml',
        'views/website_menu.xml',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
