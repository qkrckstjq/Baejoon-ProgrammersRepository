class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        
        stack = []
        for num in nums:
            stack.append([num])
            
        result = []
        
        while len(stack) != 0:
            cur_nums = stack.pop()
            for num in nums:
                if num not in cur_nums:
                    temp_nums = list(cur_nums)
                    temp_nums.append(num)
                    stack.append(temp_nums)
                if len(cur_nums) == len(nums):
                    result.append(temp_nums)
                    break
        
        return result