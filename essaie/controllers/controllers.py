# -*- coding: utf-8 -*-
# from odoo import http


# class Essaie(http.Controller):
#     @http.route('/essaie/essaie', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/essaie/essaie/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('essaie.listing', {
#             'root': '/essaie/essaie',
#             'objects': http.request.env['essaie.essaie'].search([]),
#         })

#     @http.route('/essaie/essaie/objects/<model("essaie.essaie"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('essaie.object', {
#             'object': obj
#         })

