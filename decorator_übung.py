# wrapper funtion
"""
def decorator(func):
	print("in decorator")
	def wrapper(*args, **kwargs):
		print("in wrapper")
		return func(*args, **kwargs)
	return wrapper

@decorator
def sum_num(nums):
	print("in sum_num")
	return sum(nums)

print(sum_num([1, 2, 3]))"""

# debugg_decorator
def debugger(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except (ValueError, TypeError, AttributeError) as e:
			print(f"Error: {func.__name__}: {e}")
			return None
	return wrapper


@debugger
def sum_num(nums):
	return sum(nums)

print(sum_num('test'))