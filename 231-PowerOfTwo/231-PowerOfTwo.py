# Last updated: 2/5/2026, 7:42:40 AM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&-n)==n