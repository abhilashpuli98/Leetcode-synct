# Last updated: 2/5/2026, 7:44:49 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return  str(x)==str(x)[::-1]