const double prob_succ_r1 = 0.99;


module robot1Task
	fail: bool init false;
	//Tasks
	[T1] (fail=false) -> prob_succ_r1 : (fail'=false) + (1-prob_succ_r1) : (fail'=true);
	[T2] (fail=false) -> prob_succ_r1 : (fail'=false) + (1-prob_succ_r1) : (fail'=true);
endmodule


module robot1Travelling
	location:[0..3] init 0;
	//Tasks
	[T1] (location=0) & (fail=false) -> (location'=1); //init loc=0
	[T2] (location=0) & (fail=false) -> (location'=2); //init loc=0
	[T2] (location=1) & (fail=false) -> (location'=2);
	[T3] (location=1) -> (location'=3); //goal loc=3
	[T1] (location=2) & (fail=false) -> (location'=1);
	[T3] (location=2) -> (location'=3); //goal  oc=3
endmodule
