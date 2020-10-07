import itertools



def get_number_of_tasks(CompositeTasks, Allocates):
	'''Get total number of tasks needed, depending on the composite tasks declared in "allocate" and the amount of tasks for each composite task'''

	num_tasks_total = 0
	
	a = list(itertools.chain.from_iterable(Allocates))	# create a single list with all info in "Allocates"
	print(a)



	# Count how many times each CT is repeated
	for c in CompositeTasks:

		# check how many times the compositeTask is allocated
		times_cp_allocate = a.count(c[0])

		# check tasks needed for composite task
		number_of_tasks_in_cp = c[2].count("t")

		# multiply
		tasks_needed_for_cp_i = times_cp_allocate * number_of_tasks_in_cp


		num_tasks_total = num_tasks_total + tasks_needed_for_cp_i


	return (num_tasks_total)
		
