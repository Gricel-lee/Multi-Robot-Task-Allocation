import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Plan {
	
	public Allocate[] allocate;
	public int num_locations;
	public int num_capababilities;
	public int num_robots;
	public int num_tasks;
	public int num_ct;
	public int[] num_robots_set;//This last one depends repeats for the amount of robot types
	public Robot[] robots;
	public String name;
	
	public String run_sequence;
	public String run;
	
	public Plan(Allocate[] a, int num_loc, int num_cap, int num_r, int num_t, int num_compt, int[] ind_num_r, Robot[] robots, String p_name) throws Exception {
		this.allocate = a;
		
		
		ArrayList<String> list = new ArrayList<String>();
		
		for (Allocate alloc: a) {
			list.add( alloc.getLocation().getName() ); // create array of all locations assigned
		}
		
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();

        for (int i = 0; i < list.size(); i++) {

            String key = list.get(i);

            if (hashMap.get(key) != null) {
                int value = hashMap.get(key);
                value++;
                hashMap.put(key, value);
            } else {
                    hashMap.put(key, 1);
            }

        }
        int uniqueCount = 0;
        Iterator it = hashMap.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            if ((int) pair.getValue() == 1)
                uniqueCount++;
        }
        System.out.println(uniqueCount);
		
		
		this.num_locations = uniqueCount;	// num loc in Allocate, not num_loc
		this.num_capababilities = num_cap;
		this.num_robots = num_r;
		this.num_tasks = num_t;
		this.num_ct = num_compt;
		this.num_robots_set = ind_num_r;
		this.robots = robots;
		
		
		//Add sequence 
		// Create string :  ", exactly num_robots_type_i Robot_type_i" ... for i robot types
		String robots_string = "";
		int count = 0;
		for (Robot robot:robots) {
			String name = robot.getName(); //name of robot
			Integer num = num_robots_set[count]; // number of robot
			 //robots_string = robots_string + ", exactly " + num +" "+ name;// EXACTLY AMOUNT OF ROBOTS
			 robots_string = robots_string + ", " + num +" "+ name;// UPTO CERTAIN NUM OF ROBOTS
			 count ++;
		}
		//Run sequence
		run_sequence = "run TaskAllocation for exactly "+ num_locations +" Location, "+ num_capababilities+ " Capability, "+ num_robots+" Robot, "+ num_tasks +" Task, exactly "+ num_ct +" CompositeTask "+ robots_string;
				
		
		//##### Hard-coded 07/10/2020, working on this
		num_capababilities = 7;
		num_robots = 4;
		num_tasks = 5;
		num_ct = 3;
		run_sequence = "run TaskAllocation for exactly 2 Location, 7 Capability, exactly 4 Robot, exactly 5 Task, exactly 3 CompositeTask\n";
		//#####
		
		this.run = run_sequence;
	}
	
	public Allocate[] getAllocate() {
		   return this.allocate;
	}
	public int getNum_locations() {
		   return this.num_locations;
	}
	
	public int getNum_capababilities() {
		   return this.num_capababilities;
	}
	public int getNum_robots() {
		   return this.num_robots;
	}
	public int getNum_tasks() {
		   return this.num_tasks;
	}
	public int getNum_ct() {
		   return this.num_ct;
	}
	public int[] getNum_robots_set() {
		   return this.num_robots_set;
	}
	
	public Robot[] getRobots() {
		   return this.robots;
	}
	
	public String getName() {
		   return this.name;
	}
	
}
