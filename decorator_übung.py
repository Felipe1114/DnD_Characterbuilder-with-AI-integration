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
"""
# debugg_decorator
def debugger(func):
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except (ValueError, TypeError, AttributeError) as e:
			DebugLog.log_error(e, context="Fehler in load_rewritten_prompts, db_manager.py")
			print(f"Error: {func.__name__}: {e}")

			return None
	return wrapper


@debugger
def sum_num(nums):
	return sum(nums)

# hier sollte jetzt ein fehler gerpintet werden
# auch sollte über 'DebugLog.log_error(...)' eine fehlermeldung in 'debug.log' gespeichert werden
print(sum_num('test'))"""

from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)   # prints 'does some math'