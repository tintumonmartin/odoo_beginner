# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SchoolLibrary(http.Controller):
    @http.route('/school/school/', auth='public')
    def school(self, **kw):
        return "Hello, Students"

    @http.route('/api/json/school_student/', type='json', auth='public')
    def school_student_json(self, **kw):
        print(request.env.user)
        print(request)
        print(self)
        print(kw)
        object = request.env['school.student'].sudo().search_read([])
        # print(object)
        # object = request.env['school.teacher'].sudo().search([])
        print(object)
        # return object
        return object

    @http.route('/api/html/school_student/', type='http', auth='none', csrf=False)
    def school_student_html(self, **kw):
        print(request.env.user)
        print(request)
        print(self)
        print(kw)
        object = request.env['school.student'].sudo().search_read([])
        # print(object)
        # object = request.env['school.teacher'].sudo().search([])
        print(object)
        # return object
        return "<html><body>" + str(object) + "</body></html>"
        # return "Testing"

    @http.route('/school/school_teacher/', type='json', auth='user')
    def school_teacher(self, **kw):
        print(request.env.user)
        print(request)
        print(self)
        print(kw)
        object = request.env['school.student'].sudo().search([])
        print(object)
        object = request.env['school.teacher'].sudo().search([])
        print(object)
        # return object
        return "Hello, Students"

    @http.route('/school_library/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('school_library.listing', {
            'root': '/school_library',
            'objects': http.request.env['school.student'].search([]),
        })

    @http.route('/school_library/objects/<model("school.student"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('school_library.object', {
            'object': obj
        })
