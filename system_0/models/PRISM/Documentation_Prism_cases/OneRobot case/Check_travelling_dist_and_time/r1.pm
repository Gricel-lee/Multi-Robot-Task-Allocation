const double prob_succ_r1 = 0.99;

module robot1Travelling
	location:[0..3] init 0;
	//Tasks
	[T1] (location=0) -> (location'=1); //init loc=0
	[T2] (location=0) -> (location'=2); //init loc=0
	[T2] (location=1) -> (location'=2);
	[T3] (location=1) -> (location'=3); //goal loc=3
	[T1] (location=2) -> (location'=1);
	[T3] (location=2) -> (location'=3); //goal  oc=3
endmodule

rewards "travelling"
	[T1] (location=0) : 2; // when action T1 is taken from location=0, add 2 meters
	[T2] (location=0) : 3; // when action T2 is taken from location=0, add 3 meters
	[T2] (location=1) : 1;
	[T1] (location=2) : 1;
endrewards


rewards "time"
	[T1] (location=0) : 30; // when action T1 is taken from location=0, add 30 minutes
	[T2] (location=0) : 10; // when action T2 is taken from location=0, add 3
	[T2] (location=1) : 25;
	[T1] (location=2) : 30;
endrewards


rewards "steps"
	true : 1;
endrewards

