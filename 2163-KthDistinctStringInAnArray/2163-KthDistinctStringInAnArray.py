# Last updated: 2/5/2026, 7:40:30 AM
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct=[]
        count=0
        counter=Counter(arr)
        for item in arr:
            if counter[item]==1:
                count+=1
            if count==k:
                return item
        return ""