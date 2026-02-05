# Last updated: 2/5/2026, 7:42:17 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1.intersection(nums2))
        