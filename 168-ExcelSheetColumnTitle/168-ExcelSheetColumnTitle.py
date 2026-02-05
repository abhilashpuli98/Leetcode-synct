# Last updated: 2/5/2026, 7:43:07 AM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber>0:
            columnNumber-=1
            result.append(chr(columnNumber%26+ord('A')))
            columnNumber//=26
        return "".join(result[::-1])