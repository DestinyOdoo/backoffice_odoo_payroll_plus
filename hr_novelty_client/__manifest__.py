# -*- coding: utf-8 -*-
{
    "name": "Nómina con localización colombiana Plan Básico",
    "version": "17.0.1.0.0",
    "author": "BACKOFFICE S.A.S.",
    "website": "https://www.boffice.cloud/",
    "category": "Human Resources",
    "summary": "Cliente de Novedades con validación de licencia",
    "description": """
        Hr Novelty Client
        =================
        Módulo cliente que consume las APIs del servidor de novedades.
        
        **IMPORTANTE:** Este módulo requiere licencia válida de BackOffice.
        
        Características:
        * Validación de licencia contra servidor BackOffice
        * Gestión de novedades con protección de licencia
        * Creación de empleados, contratos y contactos
    """,
    "depends": [
        "base",
        "mail",
        "hr",
        "hr_contract",
        "hr_payroll",
        "hr_holidays",
        "base_destiny_client",
        "hr_destiny_client",
        "hr_curriculum_vitae_client",
        "recruitment_reason_client",
        "hr_recruitment_extended_client",
        "partner_destiny_client",
        "ir_attachment_s3_client",
        "hr_contract_extended_client",
        "bo_license_client",
    ],
    "images": [
        "static/description/main_screenshot.png",
        "static/description/screenshots/screen_01_paso1_instalacion.png",
        "static/description/screenshots/screen_02_paso2_config_nomina.png",
        "static/description/screenshots/screen_03_paso3_novedades.png",
        "static/description/screenshots/screen_04_placeholder.png",
    ],
    "data": [
        "security/hr_novelty_security.xml",
        "security/ir.model.access.csv",
        "security/ir.rule.xml",
        "data/motivo_talento_data.xml",
        "data/calendar_data.xml",
        "data/hr_novelty_type.xml",
        "data/hr_novelty_type_subtype.xml",
        "data/ir.sequence.xml",
        "wizard/novelty_create_contact_view.xml",
        "wizard/novelty_create_employee_view.xml",
        "wizard/novelty_create_contract_view.xml",
        "wizard/novelty_reject_wizard_view.xml",
        "views/hr_novelty_view.xml",
        "views/hr_salary_structure_type_view.xml",
        "views/hr_leave_view.xml",
        "views/hr_you_fields_view.xml",
        "views/hr_module_you_view.xml",
        "views/hr_you_type_view.xml",
        "views/motivo_talento_view.xml",
        "views/hr_employee_view.xml",
        "views/inherited_hr_leaves_view.xml",
        "views/inherited_hr_payslip_view.xml",
        "views/hr_novelty_job_view.xml",
        "views/hr_job_salary_view.xml",
        "views/inherited_hr_job_view.xml",
        "views/hr_leave_code_view.xml",
        "views/inherited_hr_contract_view.xml",
        "views/res_partner_bank_view.xml",
        "views/novelty_studies_view.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
    "external_dependencies": {
        "python": ["ip2geotools"],
    },
}
