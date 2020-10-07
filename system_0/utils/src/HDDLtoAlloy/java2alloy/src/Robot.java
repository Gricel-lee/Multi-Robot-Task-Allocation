public class Robot {
	public Capability[] capabilities;
	public String name;
	Capability[] allcapabilities;
	
	public Robot (String n, Capability[] c) {
		this.name = n;
		this.allcapabilities = c;
		this.capabilities = new Capability[c.length];
		//System.arraycopy(this.capabilities, 0, c, 0, c.length);
		System.arraycopy(c, 0, this.capabilities, 0, c.length);
	}
	
	public String getName() {
		   return this.name;
	}
	
	public int getNumCapab() {
		   return this.capabilities.length;
	}

	public Capability[] getCapabilities() {
		   return this.allcapabilities;
	}
	
	//System.out.println(this.name);
}