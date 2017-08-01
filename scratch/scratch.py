


##input (1,3), (4,7), (5,8), (8,9)
##output (1,3) (4,9)


def merge_intervals(interval_arr):
	output = []

	for i in range(len(interval_arr)):
		if output and o