# -*- coding: utf-8 -*-
from odoo import http


class SchoolLibrary(http.Controller):
    @http.route('/school/school/', auth='public')
    def school(self, **kw):
        return "Hello, Students"

    @http.route('/school/school_student/', type='json', auth='public')
    def school_student(self, **kw):
        return "Hello, Students"

    @http.route('/school_library/school_library/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('school_library.listing', {
            'root': '/school_library/school_library',
            'objects': http.request.env['school_library.school_library'].search([]),
        })

    @http.route('/school_library/school_library/objects/<model("school_library.school_library"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('school_library.object', {
            'object': obj
        })
