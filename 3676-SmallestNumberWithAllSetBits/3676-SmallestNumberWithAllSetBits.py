# Last updated: 2/5/2026, 7:39:32 AM
class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            bi=str(bin(n))[2:]
            if '0' not in bi:
                return n
            else:
                n+=1
