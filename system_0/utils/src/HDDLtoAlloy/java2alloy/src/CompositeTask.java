
public class CompositeTask {
	public String name;
	public String ID;
	public Task[] tasks;
	public int numRobots;
	
	
	public CompositeTask (String n, String id, Task[] t, int r, String constrain) {
		this.name = n;
		this.ID = id;
		this.tasks = t;//new Task[t.length];
		this.numRobots = r;
		System.arraycopy(this.tasks, 0, t, 0, t.length);	//***?? Check this later
	}
	
	// Return name
	public String getName() { return this.name; }
	
	public String getID() { return this.ID; }
	
	public Task[] getTasks() { return this.tasks; }
	
	public int getNumberTasks() {return this.tasks.length; }
	
	public int getNumberRobots() {return this.numRobots; }
	
	
	
}
