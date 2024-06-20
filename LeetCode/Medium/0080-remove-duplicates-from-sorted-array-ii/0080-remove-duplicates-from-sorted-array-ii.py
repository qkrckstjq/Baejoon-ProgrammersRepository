class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
                count = 1
            elif nums[i - 1] == nums[i]:
                if count < 2:
                    nums[idx] = nums[i]
                    count += 1
                    idx += 1
                
        return idx