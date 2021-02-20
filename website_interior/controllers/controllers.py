# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteInterior(http.Controller):
#     @http.route('/website_interior/website_interior/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_interior/website_interior/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_interior.listing', {
#             'root': '/website_interior/website_interior',
#             'objects': http.request.env['website_interior.website_interior'].search([]),
#         })

#     @http.route('/website_interior/website_interior/objects/<model("website_interior.website_interior"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_interior.object', {
#             'object': obj
#         })
