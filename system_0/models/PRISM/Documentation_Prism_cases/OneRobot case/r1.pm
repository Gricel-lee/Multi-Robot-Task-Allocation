//r1 T1 T2

label "success" = T1_done & T2_done;
const double prob_succ_r1;

const double dist_init_T1=10.5; // Distance from location (base) to location where t1 takes place;
const double dist_init_T2=10.5; // Distance from location (base) to location where t2 takes place;
const double dist_T1_T2=20.0; // Distance from location where t2 takes place;

const double average_vel_r1=1.2;// m/s

const double T1_time = 60;
const double T2_time = 30;

mdp

module robot1 
	location:[0..3] init 0;
	T1_done: bool init false;
	T2_done: bool init false;
	[T1] (!T1_done) -> prob_succ_r1 : (location'=1) & (T1_done'=true)  + (1-prob_succ_r1) : (T1_done'=T1_done);
	[T2] (!T2_done) -> prob_succ_r1 : (location'=2) & (T2_done'=true)  + (1-prob_succ_r1) : (T2_done'=T2_done);

endmodule

rewards "travelling_distance"
	[T1] (location=0) : dist_init_T1; // when action T1 is taken from location=0, add 2 meters
	[T2] (location=0) : dist_init_T2; // when action T2 is taken from location=0, add 3 meters
	[T2] (location=1) : dist_T1_T2;
	[T1] (location=2) : dist_T1_T2;
endrewards


rewards "time"
	[T1] (location=0) : dist_init_T1 * 1/average_vel_r1 + T1_time; // travelling time from T0 to T1, plus time to do T1
	[T2] (location=0) : dist_init_T2 * 1/average_vel_r1+ T2_time;  // when action T2 is taken from location=0, add 3
	[T2] (location=1) : dist_T1_T2 * 1/average_vel_r1+ T2_time; 
	[T1] (location=2) : dist_T1_T2 * 1/average_vel_r1+ T1_time; 
endrewards


rewards "steps"
	true : 1;
endrewards
