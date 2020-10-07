
public class Capability {
	public String name;
	public Task canRunTask;
	
	
	public Capability (String n, Task t) {
		this.name = n;
		this.canRunTask = t;
	}
	
	public String getName() {
		   return this.name;
	}

	public Task getCanRunTask() {
		   return this.canRunTask;
	}
	
}
