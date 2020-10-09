


def create_cell_grid(robot):
	cell = [None] * 24
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

	cell_with_robots = add_robot_init_pos(cell, robot)
	
	return(cell_with_robots)

def add_robot_init_pos(cell,robot):
	for r in robot:
		for c in cell:
			if c["id"]== r["initPos"]:
				c["initPos_robot"] = r["Alloy_robot"] #there should be a better way to do this #missing checking that no two robots are in same initial pos
	return(cell)


def main(robot):
	robot = [None] * 4
	robot[0] = {"Alloy_robot" : "MedRobot$0" , "initPos" : "c1"}
	robot[1] = {"Alloy_robot" : "MedRobot$1" , "initPos" : "c2"}
	robot[2] = {"Alloy_robot" : "CleanerRobot$0" , "initPos" : "c3"}
	robot[3] = {"Alloy_robot" : "CleanerRobot$1" , "initPos" : "c4"}

	#create cell_grid
	cell = create_cell_grid(robot)

	#Print
	print(cell)

if __name__ == '__main__':
    main()