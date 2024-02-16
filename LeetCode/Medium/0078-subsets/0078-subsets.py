class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = [([], 0)]
        
        while stack:
            cur_nums, cur_index = stack.pop()
            result.append(cur_nums)
            if cur_index > len(nums) - 1:
                continue
            for i in range(cur_index, len(nums), 1):
                temp = list(cur_nums)
                temp.append(nums[i])
                stack.append((temp, i + 1))
        return result