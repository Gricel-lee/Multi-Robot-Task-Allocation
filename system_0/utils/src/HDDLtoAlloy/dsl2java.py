'''
Description: Create java executable file from DSL and robots' database Robots_db.xml
Author: Gricel Vazquez
Last update: 23/09/2020

'''


from system_0.config import settings
from system_0.utils.utilsFunctions.Robots_db import get_number_of_robots, get_total_number_of_robots, get_total_number_of_capabilities, get_num_each_type_of_robot_in_str_format
from system_0.utils.utilsFunctions.Tasks_db import get_number_of_tasks

# Path to declaration of the system in DSL
sys = settings.DSL_SYSTEM_DECL

alloy_file = "model.als"
alloy_file_output = "alloy_results.txt"


global Tasks ; Tasks = []
global CompositeTasks ; CompositeTasks = []
global Locations ; Locations = []
global Capabilities ; Capabilities  = []
global Robots; Robots = []
global Allocates;Allocates = []
global Capability_to_task;Capability_to_task = {}

global Task ; Task = []
global CompositeTask ; CompositeTask = []
global Location ; Location = []
global Capability ; Capability  = []
global Robot; Robot = []
global Allocate;Allocate = []
global Plans; Plans = []



def javaDeclaration(javafile):
	'''Java declaration'''
	javafile.write("//package java2alloy;"); javafile.write("\n"); javafile.write("\n");
	javafile.write("//Description: Create Alloy file"); javafile.write("\n");
	javafile.write("//Last update: 24/09/2020"); javafile.write("\n");
	javafile.write("//File created automatically from dsl2java.py "); javafile.write("\n"); javafile.write("\n")
	javafile.write('public class java2alloy{');	javafile.write("\n"); javafile.write("\n")
	javafile.write('	public static void main(String[] args) throws Exception {'); javafile.write("\n"); javafile.write("\n")
	return()


def execute_line_as_code(line):


	varDSL = line.split("=")[0]
	line_execute = "global "+ varDSL +"; "+line
	exec(line_execute)
	#print(line_execute)

	return()

def checkFor(lineDSL,javafile):

	line = lineDSL.replace(" ", "") #delete all spaces

	#If Task
	if line.startswith("Task"):
		execute_line_as_code(line)
		execute_line_as_code(line)
		javafile.write('		Task {} = new Task("{}","{}");{}'.format(Task[0],Task[1],Task[2],"\n"))
		#global Tasks
		Tasks.append(Task)

	#If Capability
	elif line.startswith("Capability"):
		execute_line_as_code(line)
		javafile.write('		Capability {} = new Capability("{}",{});{}'.format(Capability[0],Capability[1],Capability[2],"\n"))
		#global Capabilities
		Capabilities.append(Capability)

	elif line.startswith("Robot"):
		execute_line_as_code(line)
		javafile.write('		Robot {} = new Robot("{}", new Capability[] {});{}'.format(Robot[0],Robot[1],Robot[2],"\n"))
		#global Robots
		Robots.append(Robot)

	elif line.startswith("CompositeTask"):
		execute_line_as_code(line)
		#Create_second_ID_needed_for_java
		ID2 = (CompositeTask[0]).upper().replace("_","")  # delete later	, e.g., before in DSL:	CompositeTask = ["ct_1 ", "vitalParamGoal", "CT1", "{t1,t2} ", "{?r}"]
		# Get tasks
		cp_t = CompositeTask[2]
		javafile.write('		CompositeTask {} = new CompositeTask("{}","{}", new Task[] {},{},"{}");{}'.format(CompositeTask[0],CompositeTask[1],ID2,cp_t,"1","NONE","\n")) # "1" is for 1 robot needed
		#global CompositeTasks
		CompositeTasks.append(CompositeTask)

	elif line.startswith("JoinCompositeTask"):
		execute_line_as_code(line)
		#Create_second_ID_needed_for_java
		ID2 = (CompositeTask[0]).upper().replace("_","")  # delete later	, e.g., before in DSL:	CompositeTask = ["ct_1 ", "vitalParamGoal", "CT1", "{t1,t2} ", "{?r}"]
		# Get tasks
		cp_t = JoinCompositeTask[2]
		# Get number of robots
		num_r = JoinCompositeTask[3].count('?r')
		# Check is "exactly or at_least"
		robot_constraint = JoinCompositeTask[4]
		# In Java, Join tasks are only CompositeTasks with more robots needed, change this later in Java
		javafile.write('		CompositeTask {} = new CompositeTask("{}","{}", new Task[] {},{},"{}");{}'.format(JoinCompositeTask[0],JoinCompositeTask[1],ID2,cp_t,num_r,robot_constraint,"\n")) # "1" is for 1 robot needed
		#global CompositeTasks
		CompositeTasks.append(JoinCompositeTask)

	elif line.startswith("Location"):
		execute_line_as_code(line)
		javafile.write('		Location {} = new Location("{}");{}'.format(Location[0],Location[1],"\n"))
		#global Locations
		Locations.append(Location)

	elif line.startswith("Allocate"):
		execute_line_as_code(line)
		javafile.write('		Allocate {} = new Allocate({},{});{}'.format(Allocate[0],Allocate[1],Allocate[2],"\n"))
		#global Allocates
		Allocates.append(Allocate)

	elif line.startswith("Plan"):
		execute_line_as_code(line)
		Plans.append(Plan)

	return()


def add_lists_DSL_to_java_file(javafile):
	# Add list Tasks
	string = "{" + ','.join([item[0] for item in Tasks]) + "}"	# get list of tasks
	string = '		Task[] tasks = new Task[]' + string + ";"
	javafile.write(string); javafile.write("\n")

	# Add list Composite Tasks
	string = "{" + ','.join([item[0] for item in CompositeTasks]) + "}"	# get list 
	string = '		CompositeTask[] compositeTasks = new CompositeTask[]' + string + ";"
	javafile.write(string); javafile.write("\n")

	# Add list Locations
	string = "{" + ','.join([item[0] for item in Locations]) + "}"	# get list
	string = '		Location[] rooms = new Location[]' + string + ";"
	javafile.write(string); javafile.write("\n")

	# Add list Capabilities
	string = "{" + ','.join([item[0] for item in Capabilities]) + "}"	# get list 
	string = '		Capability[] capabilities = new Capability[]' + string + ";"
	javafile.write(string); javafile.write("\n")

	# Add list Robots
	string = "{" + ','.join([item[0] for item in Robots]) + "}"	# get list 
	string = '		Robot[] robots = new Robot[]' + string + ";"
	javafile.write(string); javafile.write("\n")

	# Add list Allocate
	string = "{" + ','.join([item[0] for item in Allocates]) + "}"	# get list 
	string = '		Allocate[] allocate = new Allocate[]' + string + ";"
	javafile.write(string); javafile.write("\n")



def add_Plan(javafile):

		for plan in Plans:
			num_locations  = len(Locations)
			num_capabilities = get_total_number_of_capabilities(Robots) # for each robot in DSL declaration, check capabilities in database
			num_robots_total = get_total_number_of_robots()
			num_tasks = get_number_of_tasks(CompositeTasks,Allocates)
			num_ct = len(Allocates)	# amount of compound tasks allocated
			num_robots = get_num_each_type_of_robot_in_str_format(Robots)
			
			stringp = '		int[] individual_num_robots = new int[]{};'.format(num_robots) 	# print variable: num_robots
			javafile.write(stringp); javafile.write("\n")									# print variable: num_robot
			# Add Plan
			javafile.write('\n		// Plan is formed by: (allocate, num_locations, num_capababilities, num_robots, num_tasks, num_ct, num_robots*, robots[], name)   *This last one depends repeats for the amount of robot types'); javafile.write("\n")
			stringp = '		Plan {} = new Plan({},{},{},{},{},{} {},"Plan1");'.format(plan[0],"allocate",num_locations,num_capabilities,num_robots_total,num_tasks,num_ct,",individual_num_robots,robots",plan[0])
			#print("FUCK3: ",stringp)
			javafile.write(stringp); javafile.write("\n")
		return()



	
def add_Create_Alloy(javafile):
	#Add Create Alloy
	javafile.write('\n		// Create alloy file'); javafile.write("\n")
	string = '		Alloy.createAlloyFile(tasks, compositeTasks, rooms, capabilities,robots,allocate,{},"{}");'.format(Plans[0][0],alloy_file)	# So far, just one plan allowed
	javafile.write(string); javafile.write("\n")	
	return()

	
def add_Run_Alloy(javafile):
	# Run Alloy file
	javafile.write('\n		// Run alloy file'); javafile.write("\n")
	string = '		Alloy.runFile("{}","{}");'.format(alloy_file,alloy_file_output)
	javafile.write(string); javafile.write("\n")	
	return()

def add_end_java_file(javafile):
	javafile.write('	}'); javafile.write("\n");
	javafile.write('}'); javafile.write("\n");
	return()



def create_java_file(dslfile , javafile):
	# Java declaration
	javaDeclaration(javafile) 

	# Parse dsl file
	dsl = dslfile.readlines()
	for line in dsl:
		checkFor(line,javafile)

	# Add lists on Java file
	add_lists_DSL_to_java_file(javafile)

	#Add Plan
	add_Plan(javafile)

	#Add Create Alloy
	add_Create_Alloy(javafile)

	#Add Run Alloy
	add_Run_Alloy(javafile)

	add_end_java_file(javafile)

	return()


def dsl_to_java():
	'''Main class stating the steps to create the Java file'''
	# Open dsl file
	dslfile = open(sys,'r')
	# Create .java file
	javafile = open('java2alloy\\src\\java2alloy.java', 'w')
	# Create java file from dsl
	create_java_file(dslfile , javafile)
	# Close file
	javafile.close()
	return()


def main():
	dsl_to_java()


if __name__ == '__main__':
	main()
