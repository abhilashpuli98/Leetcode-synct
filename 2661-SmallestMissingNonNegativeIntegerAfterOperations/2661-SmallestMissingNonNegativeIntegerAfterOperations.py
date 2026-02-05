# Last updated: 2/5/2026, 7:40:10 AM
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
       freq=Counter(num%value for num in nums)
       for i in range(len(nums)+1):
        if freq[i%value]==0:
            return i
        freq[i%value]-=1 