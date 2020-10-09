## NO JOINT TASKS IN ROBOT:
### CASE 1: for single robot file [no join composite task, one task]
RESULT: directly assign task to robot

### CASE 2: for single robot file [no join composite task, multiple task]
RESULT: check folder **OneRobot case** 

## JOINT TASK(S) IN ROBOT:

### CASE 3: for join tasks
RESULT: check folder **MultipleRobots case**

Use transitive closure to get all robots that must be modelled in a single PRISM model.

	#STEP 1 : get chain of robots sharing composite tasks
	# Eg.:
	#Star at R1
		#R1 - JT1  T2   T4
	#For each composite task check robots, e.g.:
		#R1 - JT1  T2   T4
		#R2 - JT1            T3


		#R1 - JT1  T2   T4   JT3
		#R2 - JT1                 T3
		#R3 -                JT3      T5


	#For each robot chained, do the same, e.g.:
		#R1 - JT1  T2
		#R2 - JT1       JT2
		#R5 -           JT2
		#R6 -           JT2  JT3
		#R9 -                JT3  T1

	# Save robots chained if do not exist:
	#R_chains = [[R1,R2,R5,R6,R9],...]

	# Do same with R2,R3...



    
    
    
