# Last updated: 2/5/2026, 7:45:02 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        left=0
        charSet={}
        for right,char in enumerate(s):
            if char in charSet and charSet[char]>=left:
                left=charSet[char]+1
            charSet[char]=right
            maxi=max(maxi,right-left+1)
        return maxi
                