from functools import reduce

def max_average_sub(l, k):
	current_max = end_max = l[0:k]
	for x in l[k:]:
		pot = current_max[1:].append(x)
		current_max = max(reduce(lambda x, y: x+y, current_max), reduce(lambda x, y: x+y, pot))
max_average_sub([1,12,-5,-6,50,3], 4)