# Last updated: 2/5/2026, 7:39:45 AM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 for val in nums if val%3!=0])
