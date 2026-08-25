class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        dup = set(nums)
        origin = k
        while k in dup:
            k += origin
        return k