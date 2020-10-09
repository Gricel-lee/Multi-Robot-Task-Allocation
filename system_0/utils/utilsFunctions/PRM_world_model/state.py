import PRM


def init_grid_cells():
	
	cell = [None] * 24

	#cell[i] = cell_id, [N,S,R,L] possible actions , room_name, (x,y) center position
	cell[0] = {"id" : "c1" , "actions" : [0,0,1,0] , "room_name" : "warehouse" , "pos" :  (5,5) , "occupied" : False}
	cell[1] = {"id" : "c2" , "actions" : [1,0,1,1] , "room_name" : "warehouse" , "pos" :  (15,5) , "occupied" : False}
	cell[2] = {"id" : "c3" , "actions" : [0,0,1,1] , "room_name" : "warehouse" , "pos" :  (25,5) , "occupied" : False}
	cell[3] = {"id" : "c4" , "actions" : [0,0,0,1] , "room_name" : "warehouse" , "pos" :  (35,5) , "occupied" : False}
	cell[4] = {"id" : "c5" , "actions" : [0,0,1,0] , "room_name" : "room6" , "pos" :  (5,15) , "occupied" : False}
	cell[5] = {"id" : "c6" , "actions" : [1,1,1,1] , "room_name" : "hall" , "pos" :  (15,15) , "occupied" : False}
	cell[6] = {"id" : "c7" , "actions" : [1,0,1,1] , "room_name" : "room2" , "pos" :  (25,15) , "occupied" : False}
	cell[7] = {"id" : "c8" , "actions" : [1,0,0,1] , "room_name" : "room2" , "pos" :  (35,15) , "occupied" : False}
	cell[8] = {"id" : "c9" , "actions" : [0,0,1,0] , "room_name" : "room5" , "pos" :  (5,25) , "occupied" : False}
	cell[9] = {"id" : "c10" , "actions" : [1,1,1,1] , "room_name" : "hall" , "pos" :  (15,25) , "occupied" : False}
	cell[10] = {"id" : "c11" , "actions" : [0,1,1,1] , "room_name" : "room2" , "pos" :  (25,25) , "occupied" : False}
	cell[11] = {"id" : "c12" , "actions" : [0,1,0,1] , "room_name" : "room2" , "pos" :  (35,25) , "occupied" : False}
	cell[12] = {"id" : "c13" , "actions" : [0,0,1,0] , "room_name" : "room4" , "pos" :  (5,35) , "occupied" : False}
	cell[13] = {"id" : "c14" , "actions" : [1,1,1,1] , "room_name" : "hall" , "pos" :  (15,35) , "occupied" : False}
	cell[14] = {"id" : "c15" , "actions" : [1,0,1,1] , "room_name" : "room1" , "pos" :  (25,35) , "occupied" : False}
	cell[15] = {"id" : "c16" , "actions" : [1,0,0,1] , "room_name" : "room2" , "pos" :  (35,35) , "occupied" : False}
	cell[16] = {"id" : "c17" , "actions" : [0,0,1,0] , "room_name" : "room3" , "pos" :  (5,45) , "occupied" : False}
	cell[17] = {"id" : "c18" , "actions" : [1,1,1,1] , "room_name" : "hall" , "pos" :  (15,45) , "occupied" : False}
	cell[18] = {"id" : "c19" , "actions" : [0,1,1,1] , "room_name" : "room1" , "pos" :  (25,45) , "occupied" : False}
	cell[19] = {"id" : "c20" , "actions" : [0,1,0,1] , "room_name" : "room1" , "pos" :  (35,45) , "occupied" : False}
	cell[20] = {"id" : "c21" , "actions" : [0,0,1,0] , "room_name" : "storage" , "pos" :  (5,55) , "occupied" : False}
	cell[21] = {"id" : "c22" , "actions" : [0,1,1,1] , "room_name" : "storage" , "pos" :  (15,55) , "occupied" : False}
	cell[22] = {"id" : "c23" , "actions" : [0,1,0,0] , "room_name" : "storage" , "pos" :  (25,55) , "occupied" : False}
	cell[23] = {"id" : "c24" , "actions" : [0,0,0,1] , "room_name" : "storage" , "pos" :  (35,55) , "occupied" : False}
	return cell


def robot(num_robots,initial_cell_robots,cell):
	#Create robots vector
	robot = [None] * (num_robots) #  robots

	for i in range(num_robots):
		#robot[i] = Rid, state of robot pos,(vel_magnitude, vel_direction)
		vel_config =  {"pos": cell[initial_cell_robots[i]]["pos"], "velocity": 0 , "direction" : 0}
		robot[i] = {"id" : i , "state" : vel_config}

	return robot

def object(num_object,initial_cell_object,cell):
	#Create robots vector
	objects = [None] * (num_object) #  robots

	for i in range(num_object):
		objects[i] = {"id" : i , "pos" : cell[initial_cell_object[i]]["pos"]}

	return objects


def create_system(num_robots,initial_cell_robots,cell):

	#Create robots vector
	robots = robot(num_robots,initial_cell_robots,cell)

	return robots, cell

#Predicates 
def occupied(num_cell, cell, robot, objects):
	#search if the cell is not in Robots (later: nor objects)
	for r in range (len(robot)):
		print("hi ",r)

		if robot[r]["state"]["pos"] == cell[num_cell]["pos"]:
			print("Cell is occupied OCC")
			return True
	#search if the cell is not in Robots (later: nor objects)
	for o in range (len(objects)):
		print("hi2 ",objects[o]["pos"])

		if objects[o]["pos"] == cell[num_cell]["pos"]:
			print("Cell is occupied OCC")
		
			return True

	print("Cell is free FREE")
	return False

#consistency condition holds: for each robot state
#(x, v), we have that the corresponding block of the occupancy grid is marked occupied, and no two
#robot states have the same positions (i.e., each block of the occupancy grid is occupied by at most
#o1ne robot).

def obj(cell,object_i):

	if objects[o]["pos"] == cell[num_cell]["pos"]:
		print("Cell is occupied OCC")
		
	return True


def main():
	print(__file__ + " start!!")

	PRM.prm()

	#Number of Robots
	num_robots = 3
	pos_robot = [0,1,3] #specify initial cells starting in 0

	#Number of Objects
	num_object = 2
	pos_object = [7,15] #specify initial cells starting in 0

	#Create Occupacy Grid
	cell = init_grid_cells()

	#Create system
	[robots, occupacy_grid] = create_system(num_robots,pos_robot,cell)

	#Place objects
	objects = object(num_object,pos_object,cell)

	#Predicate occupied
	occupied(1 , cell , robots, objects)
	occupied(2 , cell , robots, objects)
	occupied(15 , cell , robots, objects)

	#Predicate obj
	#obj(cell[16],objects[0]) # check if object 0 is in cell 16
	#obj(cell[8],)

	#Time unit
	tau = 1

	#action primitives
	a = ["H","L","R","U","D"] # H keep in same cell, L left, R right, U upper and D lower cell
	#availability of a motion primitive may depend on the current state of the robot

	#move the robot to the adjacent le, right, upper, and lower blocks

	#Dynamic model of the robot evolving in tau steps

	#set of all velocity config
	V = [0,1,2] # 0 stop , 1 low, 2 high

	#def saved_costs():
	#cost(rx, ry)

if __name__ == '__main__':
    main()





