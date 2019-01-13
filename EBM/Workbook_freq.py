

# In order to create a decorator, we first need to write the function
# that will decorate the functions of interest.

# we start therefore with the sort function. 

# as a parameter we catch the method of interest itself,

# inside the decorator function we will construct a wrapper function
# which will be returned by the decorator function back to the 
# method of interest to be run. . .

# in order to catch the args and keyword args, we note that these
# already have been caught by the decorator func, and can be 
# passed to the wrapper for access by *args and **kw. 
# These can be passed back to the orig function by returning it with
# *args, **kw as params, alternatively parsing back different params
# which we do in this case, i.e. the sorted list!


def sort(func):
	def wrapper(*args, **kw):
		vals = args[0]
		print(vals)
		vals.sort()
		return func(vals)
	return wrapper



class Stats:
	# so we want this method to be wrapped by the decorator.
	# we this put the sort decorator for the mode method to be
	# passed into it, and for the ls param to be sorted in the 
	# wrapper before being parsed back as a sorted list param 
	# to the same method, i.e the mode method.
	@sort
	def mode(ls):
		appe = []
		freq = {}
		for i in ls:
			if i not in appe:
				appe.append(i)

		for i in appe:

			freq[i] = ls.count(i)
		
		return freq

	@sort
	def median(ls):
		print(ls)
		length = len(vals)

		

	def mean(ls):
		pass

if __name__ == '__main__':
	import math
	vals = [2, 0, 3, 1, 0, 1, 2, 2, 4, 8, 1, 3, 3, 12, 1, 6, 2, 5, 1]
	vals2 = Stats.median(vals)
