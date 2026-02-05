# Last updated: 2/5/2026, 7:42:01 AM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)