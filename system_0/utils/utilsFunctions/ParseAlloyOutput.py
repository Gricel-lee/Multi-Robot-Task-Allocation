'''
Description: This file requires the Alloy output file in "alloyXMLFile" and the  robots database db.Robots_db.xml
Author: Gricel Vazquez
Last update: 23/09/2020

'''

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, XML
from printXMLprettify import print_xml_prettify
import os
from Robots_db import get_robot_initPos
from xml.dom import minidom

'''Write new XML to'''
robotsXMLFile= os.path.abspath("C:\\Users\\grist\\eclipse-workspace\\SampleV2-MultiRobot-Task-Allocation\\system_0\\db\\dbgenerated\\Robots.xml")

'''Read Alloy XML'''
alloyXMLFile= os.path.abspath("C:\\Users\\grist\\eclipse-workspace\\SampleV2-MultiRobot-Task-Allocation\\system_0\\models\\alloy_example_output.xml")
alloyTree = ET.parse(alloyXMLFile)
alloyRoot = alloyTree.getroot()
alloyChildren = alloyRoot.getchildren()

'''Create new XML'''
robots_xml = Element('robots')
comment = Comment('Robots database')
robots_xml.append(comment)





def create_robots_xml():
	'''Create a xml organized by set_of_robots[name,set_of_capabilities[tasks[compositeTask[location]]]]'''
	# a) For all robots check relation "contributes_to" to get Capability
	for contributes in alloyRoot[0].findall('./field[@label="contributes"]/tuple'): 
		atom = contributes.findall('./atom')
		robot = atom[0].attrib['label']
		capability = atom[1].attrib['label']
		#print("Robot ",robot,", has capability ",capability)

		# Add robot, capability, and initial position to XML	
		if robots_xml.find('./robot/name[@name="{}"]'.format(robot)) == None: #if robot do not exist, create robot
			#print ("Robot ", robot ,". Adding robot and capability")

			# Get robot initial position
			initPos = get_robot_initPos(robot)
			children = XML('''<root><robot><name name="{}"/><initPos name="{}"/><capability name="{}"/></robot></root> '''.format(robot,initPos,capability))
			robots_xml.extend(children)

		# Add capability to existing robot in XML
		elif robots_xml.find('./robot/name[@name="{}"]'.format(robot)) != None:	#if robot already exist, add capability to robot
			#print ("Robot ", robot ," exists, adding capability ",capability)
			parent = robots_xml.find('./robot/name[@name="{}"]...'.format(robot))	# (add '...' to get the parent)
			parent.extend(XML('''<root><capability name="{}"/></root>'''.format(capability)))
			

		else:
			print("Error creating XML")

		
	# b) For all Capabilities, check "run_by" to get tasks
	for runby in alloyRoot[0].findall('./field[@label="runby"]/tuple'): #Capabilities, check "run_by" to get tasks
		atom = runby.findall('./atom')
		task = atom[0].attrib['label']
		capability = atom[1].attrib['label']

		# Add task to capability in XML
		#print("Adding task ",task," to capability ",capability)
		xml_capability = robots_xml.find('./robot/capability[@name="{}"]'.format(capability))	# search for capability
		xml_capability.extend(XML('''<root><task name="{}"/></root>'''.format(task))) # add task into capability

		# c) For all tasks check to which composite task it belong and get room
		tuple_task = alloyRoot[0].find('./field[@label="tasks"]/tuple/atom[@label="{}"]...'.format(task))	#find composite task of task in "tasks" field
		atom = tuple_task.findall('./atom')
		compositeTask = atom[0].attrib['label']

		xml_task = robots_xml.find('./robot/capability/task[@name="{}"]'.format(task))	# search for task
		xml_task.extend(XML('''<root><compositeTask name="{}"/></root>'''.format(compositeTask)))

		# d) For all locations for the composite tasks 
		tuple_location = alloyRoot[0].find('./field[@label="location"]/tuple/atom[@label="{}"]...'.format(compositeTask))	#find composite task in "location" field
		atom = tuple_location.findall('./atom')
		location = atom[1].attrib['label']	
		xml_compTask = robots_xml.find('./robot/capability/task/compositeTask[@name="{}"]'.format(compositeTask))	# search for comp task 
		xml_compTask.extend(XML('''<root><location name="{}"/></root>'''.format(location)))
	 
		# e) Add initial location of the robots ********************************


	print_xml_prettify(robots_xml) #print xml output

	# Write robots XML file 
	tree = ET.ElementTree(robots_xml)	#create tree
	root = tree.getroot()
	xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ") # write file in a readable way
	with open(robotsXMLFile, "w") as f:
	    f.write(xmlstr)

	return (robots_xml)


'''
def get_travelling_costs(robots_xml):

	# For each of the robots
	robot = robots_xml.findall('./robot')
	for r in robot:
		locations_robot_r = r.findall('./capability/task/compositeTask/location')

		# Get combination of all locations: save it as a graph G(V,E), how is this saved in python?

'''


def main():
	robots_xml = create_robots_xml()


if __name__ == '__main__':
    main()

