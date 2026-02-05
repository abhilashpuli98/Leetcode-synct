# Last updated: 2/5/2026, 7:43:26 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res^=num
        return res