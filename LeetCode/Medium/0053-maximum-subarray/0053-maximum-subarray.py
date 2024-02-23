class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + (nums[i - 1] if nums[i - 1] > 0 else 0)
            if max_num < nums[i]:
                max_num = nums[i]
        return max_num
        