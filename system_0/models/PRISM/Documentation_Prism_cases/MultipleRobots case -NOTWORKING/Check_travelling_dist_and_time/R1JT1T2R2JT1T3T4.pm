//#R1 - JT1  T2
//#R2 - JT1      T3  T4

const double prob_succ_r1 = 0.99;

module r1
	r1location:[0..3] init 0;
	//Actions from loc init
	[JT1] (r1location=0) -> (r1location'=1); //init loc=0
	[r1T2] (r1location=0) -> (r1location'=2); //init loc=0
	//Actions from JT1
	[r1T2] (r1location=1) -> (r1location'=2);
	[r1goal] (r1location=1) -> (r1location'=3); //goal loc=3
	//Actions from T2
	[JT1] (r1location=2) -> (r1location'=1);
	[r1goal] (r1location=2) -> (r1location'=3); //goal  oc=3
endmodule

module r2
	r2location:[0..5] init 0;
	//Actions from loc init
	[JT1] (r2location=0) -> (r2location'=1); //init loc=0
	[r2T3] (r2location=0) -> (r2location'=3); //init loc=0
	[r2T4] (r2location=0) -> (r2location'=4); //init loc=0
	//Actions from loc JT1
	[r2T3] (r2location=1) -> (r2location'=3);
	[r2T4] (r2location=1) -> (r2location'=4);
	[r2goal] (r2location=1) -> (r2location'=5); //goal
	//Actions from loc T3
	[JT1] (r2location=3) -> (r2location'=1);
	[r2T4] (r2location=3) -> (r2location'=4);
	[r2goal] (r2location=3) -> (r2location'=5); //goal
	//Actions from loc T4
	[JT1] (r2location=4) -> (r2location'=1);
	[r2T3] (r2location=4) -> (r2location'=3);
	[r2goal] (r2location=4) -> (r2location'=5); //goal
endmodule


rewards "r1travelling"

	[JT1] (r1location=0) : 2; // when action JT1 is taken from r1location=0, add 2 meters
	[r1T2] (r1location=0) : 1;
	[r1T2] (r1location=1) : 1;
	[JT1] (r1location=2)  : 1; // when action JT1 is taken from r1location=2, add 1 meters

endrewards

rewards "r2travelling"
	[JT1] (r2location=0) : 2; // when action T1 is taken from r2location=0, add 2 meters
	[r2T3] (r2location=0) : 3; // when action T3 is taken from r2location=0, add 3 meters
	[r2T4] (r2location=0) : 3; // when action T4 is taken from r2location=0, add 3 meters
	[r2T3] (r2location=1) : 1;
	[r2T4] (r2location=1) : 1;
	[JT1] (r2location=3) : 1;
	[r2T4] (r2location=3) : 1;
	[JT1] (r2location=4) : 1;
	[r2T3] (r2location=4) : 1;
	[JT1] (r2location=2) : 1;
endrewards

rewards "r1time"
	//[r1T1] (r1location=0) : 30; // when action T1 is taken from location=0, add 30 minutes
	//[r1T2] (r1location=0) : 10; // when action T2 is taken from location=0, add 3
	//[r1T2] (r1location=1) : 25;
	//[r1T1] (r1location=2) : 30;
endrewards

rewards "r2time"
	//[r2T1] (r2location=0) : 30; // when action T1 is taken from location=0, add 30 minutes
	//[r2T2] (r2location=0) : 10; // when action T2 is taken from location=0, add 3
	//[r2T2] (r2location=1) : 25;
	//[r2T1] (r2location=2) : 30;
endrewards

rewards "steps"
	true : 1;
endrewards