# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
	
	_inherit = 'res.users'	

	@api.model
	def create(self, vals):
		logged_uid = self.env.uid
		
		if self.env['res.users'].browse(logged_uid).has_group('base.group_system'):
			self.env.uid = 1

		user = super(User, self).create(vals)
		user.write({
				'create_uid':logged_uid,
			})
		return user