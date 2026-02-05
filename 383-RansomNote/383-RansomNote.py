# Last updated: 2/5/2026, 7:42:11 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq=[0]*26
        for i in magazine:
            freq[ord(i)-ord('a')]+=1
        for i in ransomNote:
            if freq[ord(i)-ord('a')]<1:
                return False
            else:
                freq[ord(i)-ord('a')]-=1
        return True