# -*- coding: utf-8 -*-
from odoo import http

# class SubadminUserForceCreate(http.Controller):
#     @http.route('/subadmin_user_force_create/subadmin_user_force_create/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subadmin_user_force_create/subadmin_user_force_create/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subadmin_user_force_create.listing', {
#             'root': '/subadmin_user_force_create/subadmin_user_force_create',
#             'objects': http.request.env['subadmin_user_force_create.subadmin_user_force_create'].search([]),
#         })

#     @http.route('/subadmin_user_force_create/subadmin_user_force_create/objects/<model("subadmin_user_force_create.subadmin_user_force_create"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subadmin_user_force_create.object', {
#             'object': obj
#         })