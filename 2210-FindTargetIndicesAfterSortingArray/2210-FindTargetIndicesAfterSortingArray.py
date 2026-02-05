# Last updated: 2/5/2026, 7:40:27 AM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Approach -1 return [ i for i,ele in enumerate(sorted(nums)) if ele == target]
        freq = Counter(nums)
        lt_nums = sum([f for item,f in freq.items() if item<target])
        return list(range(lt_nums,freq[target]+lt_nums))