'''
Description: Create individial PRISM models for each of the robots, and a single PRISM model for join tasks using transitive closure
Author: Gricel Vazquez & Javier Camara
Last update: 04/19/2020

'''


from system_0.config import settings
from collections import Counter

# Path to declaration of the system in DSL
sys = settings.ROBOTS_AUGMENTED_DB
sys_prism = settings.PRISM_PM_PATH

alloy_file = "model.als"
alloy_file_output = "alloy_results.txt"



def alloy2prism(modulename):
	# Open robot augmented file
	file = open(sys,'r')
	robotdb = file.readlines()


	# Check for all tasks 
	# tasks = [task1, task2 ... ] - I need to add this to compositeTask in the Robots.xml generated file
	dic_tasks = Counter(tasks)	# dictionary of tasks as keys and num of repeatitions as values, e.g. {task1: 1, task2: 3, task3: 1 }
	id = 0
	for t in dic_tasks.keys:
		
		num_robots_sharing_task = dic_tasks[t]


		if num_robots_sharing_task ==1: # If this a individual task
			create_prism_indiv_task("Robots"+id+".pm",robots)	# send robots that share task

		elif num_robots_sharing_task > 1: # If this is a JOIN TASK
			create_prism_join_task("Robots"+id+".pm",robots)	# send robots that share task
		id += 1

	# Close file
	file.close()

def create_prism_indiv_task(filename , robots):
	file = create_file(filename)
	file.close()

def create_prism_join_task(filename , robots):
	file = create_file(filename)
	file.close()


# Create file
def create_file(filename, location)
	path = os.path.abspath(location + "//" + filename)
	file = open(path, 'w')
	return (file)


def create_file():





def main():
	alloy_to_prism()


if __name__ == '__main__':
    main()
