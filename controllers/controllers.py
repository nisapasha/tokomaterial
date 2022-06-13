# -*- coding: utf-8 -*-
# from odoo import http


# class Toko-material(http.Controller):
#     @http.route('/toko-material/toko-material/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko-material/toko-material/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko-material.listing', {
#             'root': '/toko-material/toko-material',
#             'objects': http.request.env['toko-material.toko-material'].search([]),
#         })

#     @http.route('/toko-material/toko-material/objects/<model("toko-material.toko-material"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko-material.object', {
#             'object': obj
#         })
