# -*- coding: utf-8 -*-
# from odoo import http


# class RailwayReservation(http.Controller):
#     @http.route('/railway_reservation/railway_reservation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/railway_reservation/railway_reservation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('railway_reservation.listing', {
#             'root': '/railway_reservation/railway_reservation',
#             'objects': http.request.env['railway_reservation.railway_reservation'].search([]),
#         })

#     @http.route('/railway_reservation/railway_reservation/objects/<model("railway_reservation.railway_reservation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('railway_reservation.object', {
#             'object': obj
#         })
