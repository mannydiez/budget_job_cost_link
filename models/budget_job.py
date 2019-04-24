# -*- coding: utf-8 -*-
 
from odoo import api, fields, models
import logging 
log = logging.getLogger(__name__)

class job_costing_planned_amount_comparison(models.Model):
	_inherit = 'job.costing'

	@api.model
	def create(self,vals):
		
		log.critical('vals = {}'.format(vals))
		list_of_objects = []


		if vals.get('job_cost_line_ids'):
			log.critical('job_cost_line_ids = {}'.format(vals['job_cost_line_ids']))
			for record in vals['job_cost_line_ids']:
				record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
			list_of_objects = vals['job_cost_line_ids']

			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(vals['job_labour_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_labour_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
						list_of_objects.append(rec2)

			else:
				for record in vals['job_labour_line_ids']:
					record[-1]['total_cost'] = (record[-1]['hours'] * record[-1]['uom_qty'] * record[-1]['cost_price'])
				list_of_objects = vals['job_labour_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(vals['job_subcon_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_subcon_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
						list_of_objects.append(rec2)
			else:
				for record in vals['job_subcon_line_ids']:
					record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
				list_of_objects = vals['job_subcon_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_overhead_line_ids'):
			log.critical('job_overhead_line_ids = {}'.format(vals['job_overhead_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_overhead_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
						list_of_objects.append(rec2)
			else:
				for record in vals['job_subcon_line_ids']:
					record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
				list_of_objects = vals['job_overhead_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))

		if vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(vals['analytic_id']))
			analytic_obj = self.env['account.analytic.account'].browse(vals['analytic_id'])
			for record_job in list_of_objects:
				has_no_group = False
				name = False
				if analytic_obj.product_budget_lines:
					for record_acc in analytic_obj.product_budget_lines:
						name = record_job[-1]['description']
						log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
						if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
							if record_job[-1]['total_cost'] > record_acc['planned_amount']:
								raise Warning("{} exceeded!".format(name))
							has_no_group = False
							break
						else:
							has_no_group = True
					if has_no_group:
						raise Warning("{} does not have a budget line".format(name))
				else:
					raise Warning('No budget lines found!')

		res = super(job_costing_planned_amount_comparison,self).create(vals)
		return res

	@api.multi
	def write(self,vals):
		log.critical('vals = {}'.format(vals))
		list_of_objects = []
		new_vals = []

		list_of_table_name = ['job_cost_line_ids','job_labour_line_ids','job_subcon_line_ids','job_overhead_line_ids']
		for x in list_of_table_name:
			for record in vals.get(x):
				if record[-1] != False:
					new_vals.append(record)

		log.critical('new_vals = {}'.format(new_vals))
		if new_vals.get('job_cost_line_ids'):
			log.critical('job_cost_line_ids = {}'.format(new_vals['job_cost_line_ids']))
			for record in new_vals['job_cost_line_ids']:
				cost_price = record[-1].get('cost_price') or self.env['job.cost.line'].browse(record[1]).cost_price
				product_qty = record[-1].get('product_qty') or self.env['job.cost.line'].browse(record[1]).product_qty
				record[-1]['total_cost'] = cost_price * product_qty
			list_of_objects = new_vals['job_cost_line_ids']

			log.critical('list_of_objects = {}'.format(list_of_objects))
		if new_vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(new_vals['job_labour_line_ids']))
			if list_of_objects:
				for rec2 in new_vals['job_labour_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['hours'] * rec2[-1]['uom_qty'] * rec2[-1]['cost_price'])
						list_of_objects.append(rec2)

			else:
				for record in new_vals['job_labour_line_ids']:
					record[-1]['total_cost'] = (record[-1]['hours'] * record[-1]['uom_qty'] * record[-1]['cost_price'])
				list_of_objects = new_vals['job_labour_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if new_vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(new_vals['job_subcon_line_ids']))
			if list_of_objects:
				for rec2 in new_vals['job_subcon_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
						list_of_objects.append(rec2)
			else:
				for record in new_vals['job_subcon_line_ids']:
					record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
				list_of_objects = new_vals['job_subcon_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if new_vals.get('job_overhead_line_ids'):
			log.critical('job_overhead_line_ids = {}'.format(new_vals['job_overhead_line_ids']))
			if list_of_objects:
				for rec2 in new_vals['job_overhead_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						rec2[-1]['total_cost'] = (rec2[-1]['cost_price'] * rec2[-1]['product_qty'])
						list_of_objects.append(rec2)
			else:
				for record in new_vals['job_subcon_line_ids']:
					record[-1]['total_cost'] = (record[-1]['cost_price'] * record[-1]['product_qty'])
				list_of_objects = new_vals['job_overhead_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))

		if new_vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(new_vals['analytic_id']))
			analytic_obj = self.env['account.analytic.account'].browse(new_vals['analytic_id'])
			for record_job in list_of_objects:
				has_no_group = False
				name = False
				if analytic_obj.product_budget_lines:
					for record_acc in analytic_obj.product_budget_lines:
						name = record_job[-1]['description']
						log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
						if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
							if record_job[-1]['total_cost'] > record_acc['planned_amount']:
								raise Warning("{} exceeded!".format(name))
							has_no_group = False
							break
						else:
							has_no_group = True
					if has_no_group:
						raise Warning("{} does not have a budget line".format(name))
				else:
					raise Warning('No budget lines found!')

		res = super(job_costing_planned_amount_comparison,self).write(vals)
		return res