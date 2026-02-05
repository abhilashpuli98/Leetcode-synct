# Last updated: 2/5/2026, 7:43:00 AM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            n=n&(n-1)
            count+=1
        return count