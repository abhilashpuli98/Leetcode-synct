# Last updated: 2/5/2026, 7:39:20 AM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n<0 for n in nums):
            return max(nums)
        return sum([x for x in set(nums) if x>=0])