# Last updated: 2/5/2026, 7:42:31 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result=len(nums)
        for i in range(len(nums)):
                result^=nums[i]^i
        return result