# -*- coding: utf-8 -*-
# from odoo import http


# class TfiParcial(http.Controller):
#     @http.route('/tfi_parcial/tfi_parcial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tfi_parcial/tfi_parcial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tfi_parcial.listing', {
#             'root': '/tfi_parcial/tfi_parcial',
#             'objects': http.request.env['tfi_parcial.tfi_parcial'].search([]),
#         })

#     @http.route('/tfi_parcial/tfi_parcial/objects/<model("tfi_parcial.tfi_parcial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tfi_parcial.object', {
#             'object': obj
#         })
