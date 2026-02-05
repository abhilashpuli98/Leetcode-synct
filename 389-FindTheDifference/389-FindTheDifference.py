# Last updated: 2/5/2026, 7:42:10 AM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for letter in s:
            result^=(ord(letter))
        for letter in t:
            result^=(ord(letter))
        return chr(result)
        