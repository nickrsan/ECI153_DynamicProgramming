from dynamic_stage import Stage

course_1 = Stage("Course 1", [3, 5, 6, 7])
course_2 = Stage("Course 2", [5, 6, 7, 9], previous=course_1)
course_3 = Stage("Course 3", [2, 4, 7, 8], previous=course_2)
course_4 = Stage("Course 4", [6, 7, 9, 9], previous=course_3)

course_1.next = course_2
course_2.next = course_3
course_3.next = course_4

course_4.optimize()
course_1.get_optimal_values()
