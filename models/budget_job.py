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
			list_of_objects = vals['job_cost_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(vals['job_labour_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_labour_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)

			else:
				list_of_objects = vals['job_labour_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(vals['job_subcon_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_subcon_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)
			else:
				list_of_objects = vals['job_subcon_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_overhead_line_ids'):
			log.critical('job_overhead_line_ids = {}'.format(vals['job_overhead_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_overhead_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)
			else:
				list_of_objects = vals['job_overhead_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))

		if vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(vals['analytic_id']))
			analytic_obj = self.env['account.analytic.account'].browse(vals['analytic_id'])
			for record_acc in analytic_obj.product_budget_lines:
				if analytic_obj.product_budget_lines:
					for record_job in list_of_objects:
						log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
						if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
							if record_job[-1]['total_cost'] > record_acc['planned_amount']:
								raise Warning('{} exceeded! {} (job cost sheet) > {} (account.analytic)'.format(record_job['group_product_id'].name,record_job['total_cost'],record_acc['total_cost']))
				else:
					raise Warning('No budget lines found!')

		res = super(job_costing_planned_amount_comparison,self).create(vals)
		return res

	@api.multi
	def write(self,vals):
		log.critical('vals = {}'.format(vals))
		list_of_objects = []


		if vals.get('job_cost_line_ids'):
			log.critical('job_cost_line_ids = {}'.format(vals['job_cost_line_ids']))
			list_of_objects = vals['job_cost_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(vals['job_labour_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_labour_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)

			else:
				list_of_objects = vals['job_labour_line_ids']
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(vals['job_subcon_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_subcon_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)
			else:
				list_of_objects = vals['job_subcon_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_overhead_line_ids'):
			log.critical('job_overhead_line_ids = {}'.format(vals['job_overhead_line_ids']))
			if list_of_objects:
				for rec2 in vals['job_overhead_line_ids']:
					has_no_group = False
					for rec in list_of_objects:
						if rec[-1]['group_product_id'] == rec2[-1]['group_product_id']:
							rec[-1]['total_cost'] += rec2[-1]['total_cost']
							has_no_group = False
						else:
							has_no_group = True
					if has_no_group:
						list_of_objects.append(rec2)
			else:
				list_of_objects = vals['job_overhead_line_ids']
			
			log.critical('list_of_objects = {}'.format(list_of_objects))

		if vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(vals['analytic_id']))
			analytic_obj = self.env['account.analytic.account'].browse(vals['analytic_id'])
			for record_acc in analytic_obj.product_budget_lines:
				if analytic_obj.product_budget_lines:
					for record_job in list_of_objects:
						log.warning('{} == {}'.format(record_job[-1]['group_product_id'],record_acc['group_product_id'].id))
						if record_job[-1]['group_product_id'] == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job[-1]['total_cost'],record_acc['planned_amount']))
							if record_job[-1]['total_cost'] > record_acc['planned_amount']:
								raise Warning('{} exceeded! {} (job cost sheet) > {} (account.analytic)'.format(record_job['group_product_id'].name,record_job['total_cost'],record_acc['total_cost']))
				else:
					raise Warning('No budget lines found!')

		res = super(job_costing_planned_amount_comparison,self).write(vals)
		return res