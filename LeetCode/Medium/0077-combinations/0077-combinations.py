class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        result = []
        for num in range(n- (k - 1)):
            stack.append([num+1])
        
        while stack:
            cur_nums = stack.pop()
            last_num = cur_nums[-1]
            
            if len(cur_nums) == k:
                result.append(cur_nums)
                continue
            
            for num in range(last_num, n):
                temp_nums = list(cur_nums)
                temp_nums.append(num+1)
                stack.append(temp_nums)
        return result