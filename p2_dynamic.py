import numpy
from dynamic_stage import Stage

def pv_cost(quantity, years_in_future):
	"""
		So far just the quantity-based cost
	:param quantity:
	:param years_in_future:
	:return:
	"""
	cost = 100000*pow(quantity, 0.8)
	pv_cost = cost/pow((1+0.05), years_in_future)
	return pv_cost

def run_problem2(num_years, needed_trucks=4, required=(0,1,1,2,2,2)):
	matrix = [[0 for val in range(num_years)] for val in range(needed_trucks+1)]

	# make the initialization cost matrix
	for year in range(num_years):
		for index, row in enumerate(matrix):
			#if index >= required[year]:
			#	needed_now = index - required[year]
			matrix[index][year] = pv_cost(index, year)

	matrix_array = numpy.array(matrix)  # make it a numpy array so we can easily take a vertical slice

	stages = []
	for year in range(num_years):
		cost_list = matrix_array[1:, year]  # pull the column out of the matrix corresponding to this year - remove the 0 value first row (should look into how this is getting there)
		year_stage = Stage(name="Year {}".format(year), cost_benefit_list=list(cost_list), calculation_function=min, selection_constraints=required)
		year_stage.max_selections = needed_trucks
		year_stage.number = year
		stages.append(year_stage)

	for index, stage in enumerate(stages):  # make the relationships now
		if index > 0:
			stages[index].previous = stages[index-1]
		if index+1 < len(stages):  # if it's not the last one
			stages[index].next = stages[index+1]

	stages[-1].optimize()
	stages[0].get_optimal_values()


run_problem2(num_years=6)

