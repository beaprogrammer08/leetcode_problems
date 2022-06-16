class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
               freq = Counter(nums)
               return [i for i in freq if freq[i]==2]