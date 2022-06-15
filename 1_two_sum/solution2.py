#solving using dictionary to reduce time complexablity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for a, b in enumerate(nums):
            if target - b in seen_values:
                return seen_values[target - b], a

            else:
                seen_values[b] = a

