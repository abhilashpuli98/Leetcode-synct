# Last updated: 2/5/2026, 7:40:35 AM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        resultant=0
        for opr in operations:
            if opr in ["++X","X++"]:
                resultant+=1
            else:
                resultant-=1
        return resultant