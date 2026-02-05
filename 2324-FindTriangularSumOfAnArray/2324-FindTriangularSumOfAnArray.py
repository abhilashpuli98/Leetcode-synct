# Last updated: 2/5/2026, 7:40:22 AM
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """n=len(nums)
        Newnums=[]
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            for i in range(len(nums)-1):
                Newnums.append((nums[i]+nums[i+1])%10)
            nums=Newnums
            Newnums=[]
        return nums[0]"""
        if len(nums)==1:
            return nums[0]
        newNums=[0]*(len(nums)-1)
        for i in range(len(nums)-1):
            newNums[i]=(nums[i]+nums[i+1])%10
        return self.triangularSum(newNums)
