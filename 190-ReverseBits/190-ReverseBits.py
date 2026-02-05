# Last updated: 2/5/2026, 7:43:02 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        result=""
        for i in range(32):
            result+='1' if (n>>i)&1 else '0'
        return int(result,2)