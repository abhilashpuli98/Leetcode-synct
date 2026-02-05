# Last updated: 2/5/2026, 7:41:56 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for val in nums:
            if val==1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi