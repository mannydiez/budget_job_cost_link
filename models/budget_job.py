# -*- coding: utf-8 -*-
 
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging 
log = logging.getLogger(__name__)

class job_costing_planned_amount_comparison(models.Model):
	_inherit = 'job.costing'

	# @api.model
	# def create(self,vals):
		
	# 	log.critical('vals = {}'.format(vals))
	# 	list_of_objects = []


	# 	if vals.get('job_cost_line_ids'):
	# 		log.critical('job_cost_line_ids = {}'.format(vals['job_cost_line_ids']))
	# 		for record in vals['job_cost_line_ids']:
	# 			record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
	# 		list_of_objects = vals['job_cost_line_ids']

	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if vals.get('job_labour_line_ids'):
	# 		log.critical('job_labour_line_ids = {}'.format(vals['job_labour_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in vals['job_labour_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						rec[-1]['total_cost'] += (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					rec2[-1]['total_cost'] = (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
	# 					list_of_objects.append(rec2)

	# 		else:
	# 			for record in vals['job_labour_line_ids']:
	# 				record[-1]['total_cost'] = (record[-1]['hours'] * record[-1]['uom_qty'] * record[-1]['cost_price'])
	# 			list_of_objects = vals['job_labour_line_ids']
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if vals.get('job_subcon_line_ids'):
	# 		log.critical('job_subcon_line_ids = {}'.format(vals['job_subcon_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in vals['job_subcon_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
	# 					list_of_objects.append(rec2)
	# 		else:
	# 			for record in vals['job_subcon_line_ids']:
	# 				record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
	# 			list_of_objects = vals['job_subcon_line_ids']
			
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if vals.get('job_overhead_line_ids'):
	# 		log.critical('job_overhead_line_ids = {}'.format(vals['job_overhead_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in vals['job_overhead_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
	# 					list_of_objects.append(rec2)
	# 		else:
	# 			for record in vals['job_subcon_line_ids']:
	# 				record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
	# 			list_of_objects = vals['job_overhead_line_ids']
			
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))

	# 	if vals.get('analytic_id'):
	# 		log.critical('analytic_id = {}'.format(vals['analytic_id']))
	# 		analytic_obj = self.env['account.analytic.account'].browse(vals['analytic_id'])
	# 		for record_job in list_of_objects:
	# 			has_no_group = False
	# 			name = False
	# 			if analytic_obj.product_budget_lines:
	# 				for record_acc in analytic_obj.product_budget_lines:
	# 					name = record_job[-1]['description']
	# 					log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
	# 					if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
	# 						log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
	# 						if record_job[-1]['total_cost'] > record_acc['planned_amount']:
	# 							raise UserError(_("{} exceeded!".format(name)))
	# 						has_no_group = False
	# 						break
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					raise UserError(_("{} does not have a budget line".format(name)))
	# 			else:
	# 				raise UserError(_('No budget lines found!'))

	# 	res = super(job_costing_planned_amount_comparison,self).create(vals)
	# 	return res

	@api.model
	def create(self,vals):
		log.critical('self = {}'.format(self))
		log.critical('vals = {}'.format(vals))
		
		res = super(job_costing_planned_amount_comparison,self).create(vals)
		log.critical('res = {}'.format(res))
		list_of_objects = []
		list_of_table_name = ['job_cost_line_ids','job_labour_line_ids','job_subcon_line_ids','job_overhead_line_ids']
		for record in res:
			for table in list_of_table_name:
				# log.critical('record[table] = {}'.format(record[table]))
				if record[table]:
					for rec in record[table]:
						# log.warning('rec = {}'.format(rec))
						has_no_group = False
						if list_of_objects:
							for obj in list_of_objects:
								# log.warning('obj = {}'.format(obj))
								# log.warning('{} = {}'.format(obj['group_product_id'].id,rec.group_product_id.id))

								if obj['group_product_id'].id == rec.group_product_id.id:
									obj['total_cost'] += rec.total_cost
									has_no_group = False
								else:
									has_no_group = True
						else:
							has_no_group = True
						if has_no_group:
							# log.warning('has_no_group = {}'.format(has_no_group))
							list_of_objects.append({'group_product_id':rec.group_product_id,'total_cost':rec.total_cost})
							
			# log.critical('list_of_objects = {}'.format(list_of_objects))
			if record.analytic_id:
				for record_job in list_of_objects:
					has_no_group = False
					if record.analytic_id.product_budget_lines:
						for record_acc in record.analytic_id.product_budget_lines:
							# log.warning('{} == {}'.format(record_job['group_product_id'].id,record_acc['group_product_id'].id))
							if record_job['group_product_id'].id == record_acc['group_product_id'].id:
								# log.warning('{} > {}'.format(record_job['total_cost'],record_acc['planned_amount']))
								if record_job['total_cost'] > record_acc['planned_amount']:
									raise UserError(_("{} exceeded!".format(record_job['group_product_id'].name)))
								has_no_group = False
								break
							else:
								has_no_group = True
						if has_no_group:
							# raise Warning("{} does not have a budget line".format(record_job['group_product_id'].name))
							raise UserError(_('{} does not have a budget line'.format(record_job['group_product_id'].name)))
					else:
						# raise Warning('No budget lines found!')
						raise UserError(_('No budget lines found!'))
		



		return res

	@api.multi
	def write(self,vals):

		# log.critical('vals = {}'.format(vals))
		# log.critical('self.job_cost_line_ids = {}'.format(self.job_cost_line_ids))
		# log.critical('self.job_labour_line_ids = {}'.format(self.job_labour_line_ids))
		# log.critical('self.job_subcon_line_ids = {}'.format(self.job_subcon_line_ids))
		# log.critical('self.job_overhead_line_ids = {}'.format(self.job_overhead_line_ids))
		res = super(job_costing_planned_amount_comparison,self).write(vals)
		# log.critical('res = {}'.format(res))
		# log.critical('self.job_cost_line_ids = {}'.format(self.job_cost_line_ids))
		# log.critical('self.job_labour_line_ids = {}'.format(self.job_labour_line_ids))
		# log.critical('self.job_subcon_line_ids = {}'.format(self.job_subcon_line_ids))
		# log.critical('self.job_overhead_line_ids = {}'.format(self.job_overhead_line_ids))
		list_of_objects = []
		list_of_table_name = ['job_cost_line_ids','job_labour_line_ids','job_subcon_line_ids','job_overhead_line_ids']
		for record in self:
			for table in list_of_table_name:
				# log.critical('record[table] = {}'.format(record[table]))
				if record[table]:
					for rec in record[table]:
						# log.warning('rec = {}'.format(rec))
						has_no_group = False
						if list_of_objects:
							for obj in list_of_objects:
								# log.warning('obj = {}'.format(obj))
								# log.warning('{} = {}'.format(obj['group_product_id'].id,rec.group_product_id.id))

								if obj['group_product_id'].id == rec.group_product_id.id:
									obj['total_cost'] += rec.total_cost
									has_no_group = False
								else:
									has_no_group = True
						else:
							has_no_group = True
						if has_no_group:
							# log.warning('has_no_group = {}'.format(has_no_group))
							list_of_objects.append({'group_product_id':rec.group_product_id,'total_cost':rec.total_cost})
							
			# log.critical('list_of_objects = {}'.format(list_of_objects))
			if record.analytic_id:
				for record_job in list_of_objects:
					has_no_group = False
					if record.analytic_id.product_budget_lines:
						for record_acc in record.analytic_id.product_budget_lines:
							# log.warning('{} == {}'.format(record_job['group_product_id'].id,record_acc['group_product_id'].id))
							if record_job['group_product_id'].id == record_acc['group_product_id'].id:
								# log.warning('{} > {}'.format(record_job['total_cost'],record_acc['planned_amount']))
								if record_job['total_cost'] > record_acc['planned_amount']:
									raise UserError(_("{} exceeded!".format(record_job['group_product_id'].name)))
								has_no_group = False
								break
							else:
								has_no_group = True
						if has_no_group:
							# raise Warning("{} does not have a budget line".format(record_job['group_product_id'].name))
							raise UserError(_('{} does not have a budget line'.format(record_job['group_product_id'].name)))
					else:
						# raise Warning('No budget lines found!')
						raise UserError(_('No budget lines found!'))
		return res

	# @api.multi
	# def write(self,vals):
	# 	log.critical('self = {}'.format(self))
	# 	log.critical('vals = {}'.format(vals))
	# 	list_of_objects = []
	# 	new_vals = {}

	# 	list_of_table_name = ['job_cost_line_ids','job_labour_line_ids','job_subcon_line_ids','job_overhead_line_ids']
	# 	for x in list_of_table_name:
	# 		if x in vals:
	# 			new_vals[x] = []
	# 			for record in vals[x]:
	# 				if record[-1] != False:
	# 					new_vals[x].append(record)

	# 	log.critical('new_vals = {}'.format(new_vals))
	# 	if new_vals.get('job_cost_line_ids'):
	# 		log.critical('job_cost_line_ids = {}'.format(new_vals['job_cost_line_ids']))
	# 		for record in new_vals['job_cost_line_ids']:
	# 			cost_price = record[-1].get('cost_price') or self.env['job.cost.line'].browse(record[1]).cost_price
	# 			product_qty = record[-1].get('product_qty') or self.env['job.cost.line'].browse(record[1]).product_qty
	# 			record[-1]['total_cost'] = cost_price * product_qty
	# 		list_of_objects = new_vals['job_cost_line_ids']

	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if new_vals.get('job_labour_line_ids'):
	# 		log.critical('job_labour_line_ids = {}'.format(new_vals['job_labour_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in new_vals['job_labour_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 						uom_qty = rec2[-1].get('uom_qty') or self.env['job.cost.line'].browse(rec2[1]).uom_qty
	# 						hours = rec2[-1].get('hours') or self.env['job.cost.line'].browse(rec2[1]).hours

	# 						rec[-1]['total_cost'] += (hours * uom_qty * cost_price)
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 					uom_qty = rec2[-1].get('uom_qty') or self.env['job.cost.line'].browse(rec2[1]).uom_qty
	# 					hours = rec2[-1].get('hours') or self.env['job.cost.line'].browse(rec2[1]).hours

	# 					rec2[-1]['total_cost'] = (hours * uom_qty * cost_price)
	# 					list_of_objects.append(rec2)

	# 		else:
	# 			for record in new_vals['job_labour_line_ids']:
	# 				cost_price = record[-1].get('cost_price') or self.env['job.cost.line'].browse(record[1]).cost_price
	# 				uom_qty = record[-1].get('uom_qty') or self.env['job.cost.line'].browse(record[1]).uom_qty
	# 				hours = record[-1].get('hours') or self.env['job.cost.line'].browse(record[1]).hours

	# 				record[-1]['total_cost'] = (hours * uom_qty * record)
	# 			list_of_objects = new_vals['job_labour_line_ids']
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if new_vals.get('job_subcon_line_ids'):
	# 		log.critical('job_subcon_line_ids = {}'.format(new_vals['job_subcon_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in new_vals['job_subcon_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 						product_qty = rec2[-1].get('product_qty') or self.env['job.cost.line'].browse(rec2[1]).product_qty
	# 						rec[-1]['total_cost'] += (cost_price * product_qty)
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 					product_qty = rec2[-1].get('product_qty') or self.env['job.cost.line'].browse(rec2[1]).product_qty
	# 					rec2[-1]['total_cost'] = (cost_price * product_qty)
	# 					list_of_objects.append(rec2)
	# 		else:
	# 			for record in new_vals['job_subcon_line_ids']:
	# 				cost_price = record[-1].get('cost_price') or self.env['job.cost.line'].browse(record[1]).cost_price
	# 				product_qty = record[-1].get('product_qty') or self.env['job.cost.line'].browse(record[1]).product_qty
	# 				record[-1]['total_cost'] = cost_price * product_qty
	# 			list_of_objects = new_vals['job_subcon_line_ids']
			
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	if new_vals.get('job_overhead_line_ids'):
	# 		log.critical('job_overhead_line_ids = {}'.format(new_vals['job_overhead_line_ids']))
	# 		if list_of_objects:
	# 			for rec2 in new_vals['job_overhead_line_ids']:
	# 				has_no_group = False
	# 				for rec in list_of_objects:
	# 					if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
	# 						cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 						product_qty = rec2[-1].get('product_qty') or self.env['job.cost.line'].browse(rec2[1]).product_qty
	# 						rec[-1]['total_cost'] += (cost_price * product_qty)
	# 						has_no_group = False
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					cost_price = rec2[-1].get('cost_price') or self.env['job.cost.line'].browse(rec2[1]).cost_price
	# 					product_qty = rec2[-1].get('product_qty') or self.env['job.cost.line'].browse(rec2[1]).product_qty
	# 					rec2[-1]['total_cost'] = (cost_price * product_qty)
	# 					list_of_objects.append(rec2)
	# 		else:
	# 			for record in new_vals['job_overhead_line_ids']:
	# 				cost_price = record[-1].get('cost_price') or self.env['job.cost.line'].browse(record[1]).cost_price
	# 				product_qty = record[-1].get('product_qty') or self.env['job.cost.line'].browse(record[1]).product_qty
	# 				record[-1]['total_cost'] = cost_price * product_qty
	# 			list_of_objects = new_vals['job_overhead_line_ids']
			
	# 		log.critical('list_of_objects = {}'.format(list_of_objects))
	# 	analytic_ids = new_vals.get('analytic_id') or self.analytic_id
	# 	if analytic_ids:
	# 		log.critical('analytic_id = {}'.format(analytic_ids))
	# 		if type(analytic_ids) == type(12):
	# 			analytic_obj = self.env['account.analytic.account'].browse(analytic_ids)
	# 		else:
	# 			analytic_obj = analytic_ids
				
	# 		for record_job in list_of_objects:
	# 			has_no_group = False
	# 			name = False
	# 			if analytic_obj.product_budget_lines:
	# 				for record_acc in analytic_obj.product_budget_lines:
	# 					name = record_job[-1]['description']
	# 					log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
	# 					if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
	# 						log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
	# 						if record_job[-1]['total_cost'] > record_acc['planned_amount']:
	# 							raise Warning("{} exceeded!".format(name))
	# 						has_no_group = False
	# 						break
	# 					else:
	# 						has_no_group = True
	# 				if has_no_group:
	# 					raise Warning("{} does not have a budget line".format(name))
	# 			else:
	# 				raise Warning('No budget lines found!')

	# 	res = super(job_costing_planned_amount_comparison,self).write(vals)
	# 	return res