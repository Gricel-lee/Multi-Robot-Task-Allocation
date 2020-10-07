import java.io.*;
import java.util.List;

public class Alloy {
	private String sigDeclaration;
	private static Task[] task;
	private static CompositeTask[] compositeTask;
	private static Location[] room;
	private static Capability[] capability;
	private static Robot[] robot;
	private static Allocate[] allocate;
	private static Plan plan;
	
	private static int i;
	private static int count;
	
	private static String path2project = "C:\\Users\\grist\\eclipse-workspace\\SampleV2-MultiRobot-Task-Allocation\\system_0"; // select relative path to save the generated alloy file
	
		//Absolute path
	private static String pathResults = "C:\\Users\\grist\\eclipse-workspace\\SampleV2-MultiRobot-Task-Allocation\\system_0\\models\\";
	//Relative path
	private static String path2AlloyFile = "\\models\\";
	
	private static String path2sigDeclaration = "src/sigDeclaration.txt";
	
	private static String returnValue; 
	
	
	
	
	public static void createAlloyFile(Task[] t, CompositeTask[] ct, Location[] r_i, Capability[] cap, Robot[] r, Allocate[] a, Plan p, String alloyFileName) throws Exception {

		task = t;
		compositeTask = ct;
		room = r_i;
		capability = cap;
		robot = r;
		allocate = a;
		plan = p;
		String alloyFile = pathResults + alloyFileName;
		
		
		//Write ALLOY file code:
		System.out.println("STARTING ALLOY FILE");
		
		// a) Delete prior file
		File f1 = new File(path2AlloyFile+alloyFile);
		boolean b = f1.delete(); // if b is true, then the file has been deleted successfully
		
		// b) Create file
		BufferedWriter WriteToFile = new BufferedWriter(new FileWriter(alloyFile, true));
				
		// c) Import sig Declaration from sigDeclaration.txt
		returnValue = readTextFile(path2sigDeclaration);
		writeTextFile(alloyFile, returnValue);
		
		// c.1) Write description line
		WriteToFile.newLine();WriteToFile.newLine();
		WriteToFile.write("// Example:-----------------------------------------");
		WriteToFile.newLine();WriteToFile.newLine();
				
		
		// d) Add Tasks			e.g.: some sig CLEAN extends Task{} {disj[runby, Capability-Cleaning]}
		WriteToFile.write("// Tasks:");WriteToFile.newLine();
		for (Task task : t) {
			WriteToFile.write("some sig " + task.name + " extends Task{}"); WriteToFile.newLine();
			WriteToFile.write("{"); WriteToFile.newLine();
			WriteToFile.write("    disj[runby, Capability-"+ task.capability + "]  // "+ task.name +" tasks only run by capability "+ task.capability); WriteToFile.newLine();
			WriteToFile.write("}"); WriteToFile.newLine();
		}
		
		
		// e) Add CompositeTasks (and JointCompositeTasks)
		for (CompositeTask compositeTask : ct) {
			
			// e.1) Add Composite task
			if (compositeTask.getNumberRobots() ==1) {
				WriteToFile.write("some sig " + compositeTask.name + " extends CompositeTask{}"); WriteToFile.newLine();
				WriteToFile.write("fact { all c:" + compositeTask.name + " | #c.tasks = " + compositeTask.getNumberTasks());
				//Iterate over tasks 
				for (Task ts: compositeTask.tasks) {
					WriteToFile.write(" and not disj["+ ts.name +", c.tasks]");
				}
				WriteToFile.write("} // Composite task "+ compositeTask.name);WriteToFile.newLine();
				WriteToFile.newLine();
			}
			
			// e.2) Add Join Composite task
			if (compositeTask.getNumberRobots() >1) {
				
				int num_tasks_to_assign = compositeTask.getNumberRobots() * compositeTask.getNumberTasks(); // get num tasks needed to assign (robots * tasks)
				System.out.println( Integer.toString(compositeTask.getNumberRobots() ));
				System.out.println( Integer.toString(compositeTask.getNumberTasks() ));
				
				int num_individual_tasks_to_assing = compositeTask.getNumberRobots();	// number of tasks to assing of each task in Join tasks matches the number of robots 
				WriteToFile.write("some sig " + compositeTask.name + " extends JointCompositeTask{}"); WriteToFile.newLine();
				WriteToFile.write("fact { all jc:" + compositeTask.name + " | #jc.tasks = " + num_tasks_to_assign);
				
				//Iterate over tasks declaring how many instances of each task is needeed
				/***I havent try with multiple tasks!! This is only working for 1 task at the moment***/
				if (compositeTask.getNumberTasks() > 1) {
					System.out.println( " WARNING: NO IDEA WHAT IT WILL DO WITH MULTIPLE TASKS IN JOINTASK");
					for (Task ts: compositeTask.tasks) {
						WriteToFile.write(" and #(jc.tasks&"+ ts.name +")="+ num_individual_tasks_to_assing );
					}
				}
				//Get composite tasks
				Task[] ct_t = compositeTask.getTasks();
				WriteToFile.write(" and disj[Task");
				for (Task task_in_ct: ct_t) {
					String task_name = task_in_ct.getName();
					WriteToFile.write("-" + task_name);
				}
				WriteToFile.write(", jc.tasks]}"); WriteToFile.newLine();
				
				
				WriteToFile.newLine();
			}
			
		}
		WriteToFile.newLine();		
		
		// f) Add Rooms
		WriteToFile.write("// Rooms:");WriteToFile.newLine();
		i = 1;
		count = room.length; //num of rooms to add commas
		WriteToFile.write("one sig ");
		
		for (Location room : r_i) {
			WriteToFile.write(room.getName());
			if (i<count) {
				WriteToFile.write(", "); //num of rooms to add commas
				i = i+1;
			}
		}
		WriteToFile.write(" extends Location{}");WriteToFile.newLine();
		WriteToFile.newLine();
		
		// g) Add Capabilities
		WriteToFile.write("// Capabilities:");WriteToFile.newLine();
		for (Capability capability: cap) {
			WriteToFile.write("some sig "+ capability.getName() +" extends Capability {}");WriteToFile.newLine();
			WriteToFile.write("{"); WriteToFile.newLine();
			WriteToFile.write("    disj[canrun, Task-"+ capability.getCanRunTask().getName() +"]"); WriteToFile.write("// Capability able to run only " + capability.getCanRunTask() +" tasks");
			WriteToFile.newLine();
			WriteToFile.write("}"); WriteToFile.newLine();
		}
		WriteToFile.newLine();
		
		// h) Add Robots
		WriteToFile.write("// Robots:");WriteToFile.newLine();
		
		for (Robot robot: r) {
			WriteToFile.write("some sig "+ robot.getName() +" extends Robot {}");WriteToFile.newLine();
			WriteToFile.write("{");WriteToFile.newLine();
			
			// h.1) Add set of capabilities
			WriteToFile.write("    disj[contributes, Capability-(");
			i=1;
			count = robot.getNumCapab();
			Capability[] set_capabilities =  robot.getCapabilities();
			
			for (Capability capab: set_capabilities) {
				//WriteToFile.write("MeasuringTemp+MeasuringPressure");
				WriteToFile.write(capab.name);
				if (i<count) {
					WriteToFile.write("+");
					i = i+1;
				}
			}
			// Close capabilities
			WriteToFile.write(")] // "+ robot.getName() +" robot");WriteToFile.newLine();
			
			
			// h.2) If it is a composite task, add constrain: robot can only contribute one time for the task
			
			//Check later what I was doing with this -.-
			//i.e., if a robot has a capability required in a task in a join task:
			for (Capability capab: robot.capabilities) { //for each capability:
				
				Task cap_task = capab.getCanRunTask();
				
				for (CompositeTask ct1 : compositeTask) { //check all comp
					if (ct1.getNumberRobots() > 1) {// if join composite task
						for (Task ct1_T: ct1.getTasks()) {	// check tasks in comp
							
							if (capab.getCanRunTask() == ct1_T){
								WriteToFile.write("    #(contributes & "+ capab.getName() +")=1 // Robot can contribute only 1 capability (i.e., cannot do all task)");WriteToFile.newLine();
							}
						}
					}
					
				}
			}
			
			//Close robot declaration
			WriteToFile.write("}");WriteToFile.newLine();
		}
		
		// Close robots
		WriteToFile.newLine();
		
		
		
		// i) Add Task specification
		WriteToFile.write("// Task specification (Task allocation in relation to task.runby):");WriteToFile.newLine();
		WriteToFile.write("pred TaskAllocation{");WriteToFile.newLine();
		for (Allocate allocate: a) {
			WriteToFile.write("    one ct:"+allocate.compositeTask.name+" | #(ct.location&"+allocate.room.getName()+")=1  // Do "+allocate.compositeTask.name+" in room "+allocate.room.getName());WriteToFile.newLine();
		}
		WriteToFile.write("}");
		WriteToFile.newLine();
		
		// j) Add Task planning
		WriteToFile.write("// ):");WriteToFile.newLine();
		WriteToFile.write(p.run);
		
		
		//Close file
		WriteToFile.close();
		
		System.out.println("ALLOY FILE COMPLITED");
	}
	
	
	// Other necessary internal functions
	 public static void runFile(String alloyFileName, String resultsFile) throws IOException {//String p, String f, String r){
		 String alloyFile = pathResults + alloyFileName;
		 String absolute_path2AlloyFile = pathResults + alloyFile;
		 
		 System.out.println("RUNNING ALLOY FILE IN:\n");
		 System.out.print(absolute_path2AlloyFile + " \n \n");
		 
		// Build cmd command. Alloy command example: "java -cp alloy4.2_2015-02-22.jar edu.mit.csail.sdg.alloy4whole.ExampleUsingTheCompiler file1"
		 String cmd1 = "java -cp alloy4.2_2015-02-22.jar edu.mit.csail.sdg.alloy4whole.ExampleUsingTheCompiler " + alloyFile;
		 
		//Select how to view results: a) Terminal  OR  b) Java console
		// a) to execute in CMD/terminal and not in Java Console
		 String[] command = {"cmd","/c", "start", "cmd.exe" ,"/K"," cd.. && cd.. && cd.. && cd.. && cd models && "+ cmd1};
		// b) to execute in Java Console
		 //String[] command = {"cmd.exe", "/K"," cd src && cd models && "+ cmd1};
		 
		 
		 
		 Runtime rt = Runtime.getRuntime();
		 Process proc = rt.exec(command);
		 BufferedReader stdInput = new BufferedReader(new InputStreamReader (proc.getInputStream()));

		///Write results (xml) in path NOT WORKING
		 String s = null;
		 String str ="";
		 while ((s=stdInput.readLine()) != null) {
			 System.out.println("vjhvkgfcxjdxfgh \n");
			 //System.out.println(s); //Read output from cmd
			 str = str + s + " \n";
		 }
		 System.out.println("FILE DONE - working?");
		 
		 
		 
	 }

	 
	 
	 
	private static String readTextFile(String fileName) {
	    String returnValue = "";
	    FileReader file;
	    String line = "";
	    try {
	        file = new FileReader(fileName);
	        BufferedReader reader = new BufferedReader(file);
	                    try {
	            while ((line = reader.readLine()) != null) {
	            returnValue += line + "\n";
	            }
	                    } finally {
	                        reader.close();
	                    }
	    } catch (FileNotFoundException e) {
	        throw new RuntimeException("File not found");
	    } catch (IOException e) {
	        throw new RuntimeException("IO Error occured");
	    }
	    return returnValue;
	}
	
	

	private static void writeTextFile(String fileName, String s) throws IOException {
	    FileWriter output;
	    output = new FileWriter(fileName);
	    try {
	        BufferedWriter writer = new BufferedWriter(output);
	        writer.write(s);
	        writer.close();
	        //Close file
	        output.close();
	    } catch (IOException e) {
	        e.printStackTrace();
	    }
	    
	}



	

		private static void write(String string2write , String fileName) throws IOException {
			//Not working
			System.out.print(string2write);
			FileWriter fileWriter = new FileWriter(fileName);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			printWriter.print(string2write);
			printWriter.close();
		}
		
	
	
	
	
		
	
}