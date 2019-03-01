courses = [1,2,3,4]
days = [1,2,3,4]

number_of_days = 7

effort = [
	[0,0,0,0],
	[3,5,2,6],
	[5,6,4,7],
	[6,7,7,9],
	[7,9,8,9],
]
efforts_trans = [
	[0,3,5,6,7],
	[0,5,6,7,9],
	[0,2,4,7,8],
	[0,6,7,9,9],
 ]

def increment_single(value, max_days, floor,):
	new_value = value
	increment_next = False
	if value >= max_days:
		new_value = floor
		increment_next = True
	else:
		new_value = value + 1

	return new_value, increment_next


def increment(keys, max_days, floor=0, num_courses=4):
	course=0
	increment_next = True
	while increment_next is True:
		value = keys[course]
		new_value, increment_next = increment_single(value,max_days, floor)
		keys[course] = new_value
		course += 1

		print(keys)
		if sum(keys) == 16:
			break


	if keys[0] + keys[1] + keys[2]+ keys[3] > 7:  # just run it again if it's an invalid number of days
		keys = increment(keys,max_days, floor, num_courses)

	return keys

def brute_force(max_days=number_of_days, course_list=courses, days_per=days, efforts=efforts_trans):

	max_study_days = 4
	final_values={}
	course_keys = [0,0,0,0]
	while course_keys != [4,4,4,4]:
		value = efforts[0][course_keys[0]] + efforts[1][course_keys[1]] + efforts[2][course_keys[2]] +  efforts[3][course_keys[3]]
		num_days = course_keys[0] + course_keys[1] + course_keys[2] + course_keys[3]
		final_values[value] = course_keys
		course_keys = increment(course_keys, max_study_days)

	max_val = max(final_values.keys())
	print("{}: {}".format(max_val, final_values[max_val]))


brute_force()

