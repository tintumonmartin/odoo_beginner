# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SchoolLibrary(http.Controller):
    @http.route('/school/school/', auth='public')
    def school(self, **kw):
        return "Hello, Students"

    @http.route('/school/school_student/', type='http', auth='public')
    def school_student(self, **kw):
        print(request.env.uid)
        print(request.env.user)
        object = request.env['school.student'].sudo().search_read(
            [],
            fields=['name', 'student_identity', 'department_id', 'phone', 'address', 'mark', 'result'])
        print(object)
        print(object[0])
        return str(object[0])

    @http.route('/school/school_teacher/', type='json', auth='user')
    def school_teacher(self, **kw):
        object = request.env['school.teacher'].sudo().search_read(
            [],
            fields=['name', 'teacher_identity', 'department_id', 'phone', 'address']
        )
        return object

    @http.route('/school_library/school_library/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('school_library.listing', {
            'root': '/school_library/school_library',
            'objects': http.request.env['school.student'].search([]),
        })

    @http.route('/school_library/school_library/objects/<model("school_library.school_library"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('school_library.object', {
            'object': obj
        })
