some abstract sig Robot {
	contributes : some Capability
} 
fact { all r:Robot | disj[r.contributes, (Robot-r).contributes]} // Robot capabilities do not overlap

some abstract sig Capability {
	canrun: some Task,
	belongsto: one Robot
}
fact { all c:Capability, r:Robot | r in c.belongsto <=> c in r.contributes } 

some abstract sig Location {}

some abstract sig Task {
	runby: one Capability
} 
fact { all t:Task, c:Capability | t.runby = c => t in c.canrun} // All tasks are run by a capability able to run it

some abstract sig CompositeTask {
	tasks: some Task,
	location: one Location
}
fact { 
	all ct:CompositeTask | disj[ct.tasks, (CompositeTask-ct).tasks] // Tasks belong only to a single composite task
}

abstract sig JointCompositeTask extends CompositeTask {
}

fact { all jct:JointCompositeTask | all t:jct.tasks, t':jct.tasks-t | disj[t.runby, t'.runby] }

fact {
	Location in CompositeTask.location // All locations have some composite task running in it
	Task in Capability.canrun // All tasks are covered by some robot capability
	Task in CompositeTask.tasks // All tasks are part of a composite task
	Capability in Robot.contributes // All capabilities belong to some robot
}


// Example:-----------------------------------------

// Tasks:
some sig TEMP extends Task{}
{
    disj[runby, Capability-MeasuringTemp]  // TEMP tasks only run by capability MeasuringTemp
}
some sig PRESSURE extends Task{}
{
    disj[runby, Capability-MeasuringPressure]  // PRESSURE tasks only run by capability MeasuringPressure
}
some sig CLEAN extends Task{}
{
    disj[runby, Capability-Cleaning]  // CLEAN tasks only run by capability Cleaning
}
some sig MOVEF extends Task{}
{
    disj[runby, Capability-MovingFurniture]  // MOVEF tasks only run by capability MovingFurniture
}
some sig vitalParamGoal extends CompositeTask{}
fact { all c:vitalParamGoal | #c.tasks = 2 and not disj[TEMP, c.tasks] and not disj[PRESSURE, c.tasks]} // Composite task vitalParamGoal

some sig cleanRoom extends CompositeTask{}
fact { all c:cleanRoom | #c.tasks = 1 and not disj[CLEAN, c.tasks]} // Composite task cleanRoom

some sig moveFurnitureGoal extends JointCompositeTask{}
fact { all jc:moveFurnitureGoal | #jc.tasks = 2 and disj[Task-MOVEF, jc.tasks]}


// Rooms:
one sig RoomA, RoomB extends Location{}

// Capabilities:
some sig Cleaning extends Capability {}
{
    disj[canrun, Task-CLEAN]// Capability able to run only Task@8efb846 tasks
}
some sig MeasuringTemp extends Capability {}
{
    disj[canrun, Task-TEMP]// Capability able to run only Task@2a84aee7 tasks
}
some sig MeasuringPressure extends Capability {}
{
    disj[canrun, Task-PRESSURE]// Capability able to run only Task@a09ee92 tasks
}
some sig MovingFurniture extends Capability {}
{
    disj[canrun, Task-MOVEF]// Capability able to run only Task@30f39991 tasks
}

// Robots:
some sig CleanerRobot extends Robot {}
{
    disj[contributes, Capability-(Cleaning)] // CleanerRobot robot
}
some sig MedRobot extends Robot {}
{
    disj[contributes, Capability-(MeasuringTemp+MeasuringPressure)] // MedRobot robot
}
some sig MoveRobot extends Robot {}
{
    disj[contributes, Capability-(MovingFurniture)] // MoveRobot robot
    #(contributes & MovingFurniture)=1 // Robot can contribute only 1 capability (i.e., cannot do all task)
}

// Task specification (Task allocation in relation to task.runby):
pred TaskAllocation{
    one ct:vitalParamGoal | #(ct.location&RoomB)=1  // Do vitalParamGoal in room RoomB
    one ct:cleanRoom | #(ct.location&RoomA)=1  // Do cleanRoom in room RoomA
    one ct:moveFurnitureGoal | #(ct.location&RoomA)=1  // Do moveFurnitureGoal in room RoomA
}
// ):
run TaskAllocation for exactly 2 Location, 7 Capability, exactly 4 Robot, exactly 5 Task, exactly 3 CompositeTask
