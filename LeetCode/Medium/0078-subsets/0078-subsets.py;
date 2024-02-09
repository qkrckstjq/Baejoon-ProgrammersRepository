class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        stack = []
        index_stack = []
        
        for i in range(len(nums)):
            stack.append([nums[i]])
            index_stack.append(i)
        
        while stack:
            cur = stack.pop()
            last_index = index_stack.pop()
            result.append(list(cur))
            
            for i in range(last_index + 1, len(nums)):
                next = list(cur)
                next.append(nums[i])
                stack.append(next)
                index_stack.append(i)
        
        return result
            
                
                