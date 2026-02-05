# Last updated: 2/5/2026, 7:44:30 AM
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)