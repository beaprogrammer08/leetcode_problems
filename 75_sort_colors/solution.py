# sorted with the help selection sort method

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in range(0, len(nums)):
            for i in range(n, len(nums)):
                if nums[n] > nums[i]:
                    nums[i], nums[n] = nums[n], nums[i]

        return (nums)
