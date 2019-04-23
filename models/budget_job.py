# -*- coding: utf-8 -*-
 
from odoo import api, fields, models
import logging 
log = logging.getLogger(__name__)

class job_costing_planned_amount_comparison(models.Model):
	_inherit = 'job.costing'

	@api.model
	def create(self,vals):
		list_of_objects = []


		if vals.get('job_cost_line_ids'):
			log.critical('job_cost_line_ids = {}'.format(vals['job_cost_line_ids']))
			list_of_objects = vals['job_cost_line_ids']
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(vals['job_labour_line_ids']))
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_labour_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_labour_line_ids']
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(vals['job_subcon_line_ids']))
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_subcon_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_subcon_line_ids']
			
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_overhead_line_ids'):
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_overhead_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_overhead_line_ids']
			log.critical('job_overhead_line_ids = {}'.format(vals['job_overhead_line_ids']))
			
		log.critical('list_of_objects = {}'.format(list_of_objects))

		if vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(analytic_id))
			for record_acc in vals['analytic_id'].product_budget_lines:
				if vals['analytic_id'].product_budget_lines:
					for record_job in list_of_objects:
						log.warning('{} == {}'.format(record_job['group_product_id'].id,record_acc['group_product_id'].id))
						if record_job['group_product_id'].id == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job['total_cost'],record_acc['planned_amount']))
							if record_job['total_cost'] > record_acc['planned_amount']:
								raise Warning('{} exceeded! {} (job cost sheet) > {} (account.analytic)'.format(record_job['group_product_id'].name,record_job['total_cost'],record_acc['total_cost']))
				else:
					raise Warning('No budget lines found!')
		res = super(job_costing_planned_amount_comparison,self).create(vals)
		return res

	@api.multi
	def write(self,vals):
		list_of_objects = []


		if vals.get('job_cost_line_ids'):
			log.critical('job_cost_line_ids = {}'.format(job_cost_line_ids))
			list_of_objects = vals['job_cost_line_ids']
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_labour_line_ids'):
			log.critical('job_labour_line_ids = {}'.format(job_labour_line_ids))
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_labour_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_labour_line_ids']
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_subcon_line_ids'):
			log.critical('job_subcon_line_ids = {}'.format(job_subcon_line_ids))
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_subcon_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_subcon_line_ids']
			
		log.critical('list_of_objects = {}'.format(list_of_objects))
		if vals.get('job_overhead_line_ids'):
			if list_of_objects:
				for rec in list_of_objects:
					for rec2 in vals['job_overhead_line_ids']:
						if rec['group_product_id'].id == rec2['group_product_id']:
							rec['total_cost'] += rec2['total_cost']
			else:
				list_of_objects = vals['job_overhead_line_ids']
			log.critical('job_overhead_line_ids = {}'.format(job_overhead_line_ids))
			
		log.critical('list_of_objects = {}'.format(list_of_objects))

		if vals.get('analytic_id'):
			log.critical('analytic_id = {}'.format(analytic_id))
			for record_acc in vals['analytic_id'].product_budget_lines:
				if vals['analytic_id'].product_budget_lines:
					for record_job in list_of_objects:
						log.warning('{} == {}'.format(record_job['group_product_id'].id,record_acc['group_product_id'].id))
						if record_job['group_product_id'].id == record_acc['group_product_id'].id:
							log.warning('{} > {}'.format(record_job['total_cost'],record_acc['planned_amount']))
							if record_job['total_cost'] > record_acc['planned_amount']:
								raise Warning('{} exceeded! {} (job cost sheet) > {} (account.analytic)'.format(record_job['group_product_id'].name,record_job['total_cost'],record_acc['total_cost']))
				else:
					raise Warning('No budget lines found!')

		res = super(job_costing_planned_amount_comparison,self).write(vals)
		return res