# -*- coding: utf-8 -*-
{
    'name': "School library",
    'summary': "managing school library",
    ""
    'description': """
        Manage the school library
    """,
    'author': "My project",
    'website': "http://www.tintumon.co.in",
    'category': 'extra tools',
    'version': '0.0.1',
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/school_department_views.xml',
        'views/school_course_views.xml',
        'views/library_book_views.xml',
        'views/student_attendance_views.xml',
        'views/templates.xml',
        'report/mark_report.xml',
        'report/mark_report_template.xml',
    ],
    'application': True,
    'images': ['static/description/icon.png'],
}
