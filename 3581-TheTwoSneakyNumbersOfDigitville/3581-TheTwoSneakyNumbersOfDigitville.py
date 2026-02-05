# Last updated: 2/5/2026, 7:39:38 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq=[0]*len(nums)
        res=[]
        for num in nums:
            if freq[num]==1:
                res.append(num)
            else:
                freq[num]+=1
        return res 
