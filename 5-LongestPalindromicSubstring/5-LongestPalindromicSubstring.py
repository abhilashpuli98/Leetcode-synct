# Last updated: 2/5/2026, 7:44:56 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxi=0
        result=""
        for i in range(n):
            r=l=i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>maxi:
                    maxi=r-l+1
                    result=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>maxi:
                    maxi=r-l+1
                    result=s[l:r+1]
                l-=1
                r+=1
        return result
            