# Last updated: 2/5/2026, 7:45:01 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            seen[num]=i