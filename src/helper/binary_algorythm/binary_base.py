from pydantic import BaseModel

class BinaryBase:
	"""has a funktion with the binary binary_algorythm and finds a target: int in nums: list"""
	def __init(self, nums, target):
		self._nums = nums
		self._target = target
		
	def _binary_algo(self, nums, target):
		"""geht durch eine liste von geordnetne zahlen und findet den index der gesuchten zahl"""
		if len(nums) == 0:
			return -1
		
		mid_idx = len(nums) // 2
		
		if nums[mid_idx] == target:
			return mid_idx
		elif nums[mid_idx] < target:
			offset = mid_idx + 1
			
			return offset + self._binary_algo(nums[offset:], target)
		else:
			return self._binary_algo(nums[:mid_idx], target)
		
	def result(self) -> int:
		"""ruft _binary_algo auf und gibt liste und gesuchte zahl, als argument, weiter"""
		return self._binary_algo(self._nums, self._target)
