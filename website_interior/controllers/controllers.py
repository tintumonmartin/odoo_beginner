# -*- coding: utf-8 -*-
from odoo import http


class WebsiteInterior(http.Controller):

    # @http.route('/website_interior/website_interior/', auth='public')
    #     def index(self, **kw):
    #         return "Hello, world"

    @http.route('/website_interior/', auth='public')
    def list(self, **kw):
        return http.request.render('website_interior.listing', {
            'root': '/website_interior',
            'objects': http.request.env['school.student'].sudo().search([]),
        })

    @http.route('/website_interior/object', auth='public')
    def list_object(self, **kw):
        return http.request.render('website_interior.object', {
            'object': http.request.env['school.student'].sudo().search([], limit=1),
        })

    @http.route('/website_interior/objects/<model("school.student"):obj>/', auth='public')
    def object(self, obj, **kw):
        print(obj)
        return http.request.render('website_interior.object', {
            'object': obj
        })
