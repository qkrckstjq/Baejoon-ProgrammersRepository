class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        
        k = None
        for i in range(1, len(nums)):
            num_a = nums[i]
            num_b = sorted_arr[i]
            if num_a != num_b:              
                if k is None:
                    k = num_a & num_b
                else:
                    k = (num_a & num_b) & k
    
        return k if k is not None else 0 



    

    