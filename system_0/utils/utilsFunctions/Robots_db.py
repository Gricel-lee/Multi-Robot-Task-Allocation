'''
Description: Related to the database Robots_db.xml
Author: Gricel Vazquez
Last update: 23/09/2020

'''


from xml.etree import ElementTree as ET
import os
import itertools

# Import settings
from system_0.config import settings
robot_init_xml = os.path.abspath(settings.ROBOTS_DB)



	
def robots():
	'''This funtion contains the XML for the robots initial positions'''
	robotTree = ET.parse(robot_init_xml)
	return(robotTree)


def get_robot_initPos(robot):
	'''Get the initial position of a robot based on Robots_db.xml'''

	robotTree_InitPos = robots()	#get robots database
	r = robotTree_InitPos.findall('./robot/Alloy_robot[@name="{}"]...'.format(robot))	# (add '...' to get the parent)r = robotTree_InitPos.findall(['./robot/Alloy_robot[@name={}]...'.format(robot)])	# (add '...' to get the parent)
	initPos = r[0][1].attrib['cell']
	#print("Initial position: ",initPos," of robot: "robot)
	return initPos

def get_number_of_robots(type_robot):
	'''Return how many robots are of type type_robot'''
	robotTree = robots()
	#print(len(robotTree.findall('./robot')))
	r = robotTree.findall('./robot/DSL_robot[@type="{}"]...'.format(type_robot))
	#print("There are ",len(r)," ",type_robot," robots")
	return(len(r))

def get_total_number_of_robots():
	robotTree_InitPos = robots()	#get robots database
	robots_total_num = len(robotTree_InitPos.findall('./robot'))
	return(robots_total_num)

def get_total_number_of_capabilities(Robot):
	'''Get the number of capabilities that are required given the number of robots available (Database) and the tasks declare (DSL)'''
	robotTree_InitPos = robots()	#get robots database
	alloy_robot = robotTree_InitPos.findall('./robot/DSL_robot')
	capab = []
	num_cap = 0
	robot = list(itertools.chain.from_iterable(Robot)) # create a single list with Robot information (e.g.  ['r1', 'CleanerRobot', '{c1}', 'r2', 'MedRobot', '{c2,c3}'])

	for i in range (len(alloy_robot)): # get all Alloy_robot names
		type_robot = alloy_robot[i].attrib['type'] # get type of robot, e.g., type="MedRobot"

		#search how many capabilities declared in DSL using "robot list" (i.e., robot = list(itertools.chain.from_iterable(Robot)))
		name_index = robot.index(type_robot)
		#get next position
		cap = robot[name_index + 1]
		#obtain capabilities
		num_cap = num_cap + len(cap.split(','))

	return(num_cap)


def get_num_each_type_of_robot_in_str_format(Robots):
	num_robots = []
	# Check robots available in database of each type
	robot_types = [item[1] for item in Robots] # get list of robot types
	for type in robot_types:
		num_robots.append(str(get_number_of_robots(type)))
	num_robots = "{" + ",".join(num_robots)+ "}"
	return(num_robots)

def main():
	robotTree_InitPos = robots()
	#print(robotTree_InitPos)


if __name__ == '__main__':
    main()
