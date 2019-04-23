# -*- coding: utf-8 -*-

{
    'name': 'Budget Job Cost Link',
    'version': '0.1',
    'category': 'Sales/Accounting',
    'summary': 'Job Cost Sheets cannot exceeded Analytic Account',
    'description': """When a Job Cost Sheets created to an Analytic Account, check the Planned Amount for each Group of Product. 
    If exceeded the Planned Amount in Analytical Account, show error that tell which Group of Product exceeded Planned Amount 
    and Job Cost Sheets can’t be saved.""",
    'website':"www.hashmicro.com",
    'author': 'HashMicro / Emmanuel Diez',
    'depends': ['job_costing_management_extension','account'],
    # 'data': [
    #     'sequence/sequence.xml',
    # ],    
    'installable': True,
    'application': False,
    
}