# -*- coding: utf-8 -*-
{
    'name': "ESTK",

    'sequence': 4,
    'summary': """
        Les Formations Accréditées à l'ESTK. Diplôme Universitaire de Technologie (Bac+2), 
        Licence professionnelle, Formation continue (en cours de préparation).""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/student.xml',
        'views/classes.xml',
        'views/subject.xml',
        'views/classroom_view.xml',
        'views/reservation_views.xml',
        'views/element.xml',
        'views/filiere.xml'
        # 'wizards/attendance_import_view.xml',
        # 'wizards/student_attendance_wizard_view.xml',
        # 'views/attendance_register_view.xml',
        # 'views/attendance_sheet_view.xml',
        # 'views/attendance_line_view.xml',
        # 'views/attendance_type_view.xml',
        # 'views/attendance_session_view.xml'

        # 'wizards/students_wizard.xml',
        # 'reports/student_report.xml',
        # 'reports/teacher_report.xml',
        # 'reports/class_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
