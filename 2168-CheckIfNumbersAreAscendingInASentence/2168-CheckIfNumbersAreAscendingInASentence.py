# Last updated: 2/5/2026, 7:40:29 AM
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens=s.split()
        prevNum=-1
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                currentNumber=int(tokens[i])
                if prevNum>=currentNumber:
                    return False
                else:
                    prevNum=currentNumber
        return True

        