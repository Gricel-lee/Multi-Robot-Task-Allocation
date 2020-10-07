'''
Description: 	This is the bridge between the extender system declaration in HDDL, and the low level DSL use
				This is required as the HDDL can be extended continuously, independently on the DSL, which is related to the growing of handling variables/constraints in Alloy,PRISM and simulation
Author: Gricel Vazquez
Last update: 03/10/2020

'''


from system_0.config import settings

hhld_domain = settings.HDDL_DOMAIN
hhld_problem = settings.HDDL_PROBLEM


def parse_hddl_domain():
	hddl_domain_str = read_file_to_string(hddl_domain)

def parse_hddl_problem():
	hddl_problem_str = read_file_to_string(hddl_problem)




def read_file_to_string(file):
	with open(file, 'r') as file:
    	data = file.read().replace('\n', '')
	return data