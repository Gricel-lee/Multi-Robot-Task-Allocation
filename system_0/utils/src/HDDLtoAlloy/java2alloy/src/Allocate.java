public class Allocate {
	public CompositeTask compositeTask;
	public Location room;
	
	public Allocate(CompositeTask ct, Location r){
		this.room = r;
		this.compositeTask = ct;
		
	}
	
	public CompositeTask getCompositeTask() {
		   return this.compositeTask;
	}
	
	public Location getLocation() {
		   return this.room;
	}

}
