//package java2alloy;

//Description: Create Alloy file
//Last update: 24/09/2020
//File created automatically from dsl2java.py 

public class java2alloy{

	public static void main(String[] args) throws Exception {

		Task t1 = new Task("TEMP","MeasuringTemp");
		Task t2 = new Task("PRESSURE","MeasuringPressure");
		Task t3 = new Task("CLEAN","Cleaning");
		Task t4 = new Task("MOVEF","MovingFurniture");
		Capability c1 = new Capability("Cleaning",t3);
		Capability c2 = new Capability("MeasuringTemp",t1);
		Capability c3 = new Capability("MeasuringPressure",t2);
		Capability c4 = new Capability("MovingFurniture",t4);
		CompositeTask ct_1 = new CompositeTask("vitalParamGoal","CT1", new Task[] {t1,t2},1,"NONE");
		CompositeTask ct_2 = new CompositeTask("cleanRoom","CT2", new Task[] {t3},1,"NONE");
		CompositeTask ct_3 = new CompositeTask("moveFurnitureGoal","CT2", new Task[] {t4},2,"exactly");
		Location l_A = new Location("RoomA");
		Location l_B = new Location("RoomB");
		Robot r1 = new Robot("CleanerRobot", new Capability[] {c1});
		Robot r2 = new Robot("MedRobot", new Capability[] {c2,c3});
		Robot r3 = new Robot("MoveRobot", new Capability[] {c4});
		Allocate a_1 = new Allocate(ct_1,l_B);
		Allocate a_2 = new Allocate(ct_2,l_A);
		Allocate a_4 = new Allocate(ct_3,l_A);
		Task[] tasks = new Task[]{t1,t2,t3,t4};
		CompositeTask[] compositeTasks = new CompositeTask[]{ct_1,ct_2,ct_3};
		Location[] rooms = new Location[]{l_A,l_B};
		Capability[] capabilities = new Capability[]{c1,c2,c3,c4};
		Robot[] robots = new Robot[]{r1,r2,r3};
		Allocate[] allocate = new Allocate[]{a_1,a_2,a_4};
		int[] individual_num_robots = new int[]{2,2,2};

		// Plan is formed by: (allocate, num_locations, num_capababilities, num_robots, num_tasks, num_ct, num_robots*, robots[], name)   *This last one depends repeats for the amount of robot types
		Plan plan_1 = new Plan(allocate,2,8,6,4,3 ,individual_num_robots,robots,"Plan1");

		// Create alloy file
		Alloy.createAlloyFile(tasks, compositeTasks, rooms, capabilities,robots,allocate,plan_1,"model.als");

		// Run alloy file
		Alloy.runFile("model.als","alloy_results.txt");
	}
}
