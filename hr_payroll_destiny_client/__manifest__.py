# -*- coding: utf-8 -*-
{
    "name": "HR Payroll BackOffice Client",
    "summary": "Cliente de Nómina BackOffice con validación de licencia",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "website": "https://www.boffice.cloud/",
    "author": "BACKOFFICE S.A.S.",
    "application": False,
    "installable": True,
    "description": """
        HR Payroll BackOffice Client
        =========================
        Módulo cliente que consume las APIs del servidor de nómina BackOffice.
        
        **IMPORTANTE:** Este módulo requiere licencia válida de BackOffice.
        
        Características:
        * Validación de licencia contra servidor BackOffice
        * Cálculo de nóminas con protección de licencia
        * Gestión de acumulados y configuraciones
    """,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "hr_holidays",
        "hr_payroll_account",
        "documents_hr",
        "hr",
        "hr_contract",
        "hr_employee_extended_client",
        "hr_work_entry_contract",
        "bo_license_client",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/hr_payroll_destiny_security.xml",
        "views/hr_salary_rule_view.xml",
        "wizard/reprocess_acumulate_wizard_view.xml",
        "views/payslip_view.xml",
        "views/inherited_account_view.xml",
        "views/inherited_account_journal_view.xml",
        "views/hr_leaves_generate_view.xml",
        "views/inherited_hr_contract_view.xml",
        "views/hr_conf_acumulated_view.xml",
        "views/day_calculation_view.xml",
        "views/hr_acumulated_rules_view.xml",
        "views/hr_employee_acumulate_view.xml",
        "views/inherited_hr_employee_view.xml",
        "views/inherited_hr_leave_allocation.xml",
        "views/inherited_hr_leave.xml",
        "wizard/update_leave_details_wizard_view.xml",
        "wizard/hr_payroll_payslips_by_employees_views.xml",
        "wizard/payroll_config_reason_reject_view.xml",
        "views/inherited_hr_leave_type_view.xml",
        "views/inherited_resource_calendar_view.xml",
        "views/inherited_hr_salary_rule_category_view.xml",
        "views/hr_payroll_config_parameters_view.xml",
        "views/hr_payroll_config_view.xml",
        "views/inherited_hr_payslip_worked_days.xml",
        "data/hr.payroll.structure.type.csv",
        "data/mail_template_data.xml",
        "data/report_data.xml",
        "report/payslip_report.xml",
        "views/res_config_settings_view.xml",
    ],
    "license": "LGPL-3",
}
