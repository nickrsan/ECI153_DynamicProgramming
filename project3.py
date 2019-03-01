import numpy
from dynamic_stage import Stage

def pv_cost_power(capacity_needed, years_in_future):
	"""
		So far just the quantity-based cost
	:param quantity:
	:param years_ago:
	:return:
	"""
	cost = 10000000*pow(capacity_needed*100, 0.75)
	pv_cost = cost/pow((1+0.05), years_in_future * 5)
	return pv_cost


def run_project3(num_years, needed_HMW=69, required=(0, 10, 20, 35, 45, 51, 61, 65, 70, 69), start_year=2020):
	"""
		This seems to fail when there is a requirement on the first time period - first time period should have 0 requirement.
		I bet this is due to one of the many weird calcualtions I have this making, but I haven't tracked it down.
	:param num_years:
	:param needed_HMW:
	:param required:
	:return:
	"""
	matrix = [[0 for val in range(num_years)] for val in range(needed_HMW+1)]

	# make the initialization cost matrix
	for year in range(num_years):
		for index, row in enumerate(matrix):
			#if index >= required[year]:
			#	needed_now = index - required[year]
			matrix[index][year] = pv_cost_power(index, year)

	matrix_array = numpy.array(matrix)  # make it a numpy array so we can easily take a vertical slice

	stages = []
	for year in range(num_years):
		cost_list = matrix_array[1:, year]  # pull the column out of the matrix corresponding to this year - remove the 0 value first row (should look into how this is getting there)
		year_stage = Stage(name="Year {}".format(year*5+start_year), cost_benefit_list=list(cost_list), calculation_function=min, selection_constraints=required)
		year_stage.max_selections = needed_HMW
		year_stage.number = year
		stages.append(year_stage)

	for index, stage in enumerate(stages):  # make the relationships now
		if index > 0:
			stages[index].previous = stages[index-1]
		if index+1 < len(stages):  # if it's not the last one
			stages[index].next = stages[index+1]

	stages[-1].optimize()
	stages[0].get_optimal_values()

run_project3(9)