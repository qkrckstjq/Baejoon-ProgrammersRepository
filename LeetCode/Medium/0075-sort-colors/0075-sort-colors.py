class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.merge_sort(nums, 0, len(nums) - 1)
    def merge_sort(self, arr, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid + 1, end)
        self.sorting(arr, start, mid, mid + 1, end)
    
    def sorting(self, arr, i, i_end, j, j_end):
        result = []
        start = i
        end = j_end
        while i <= i_end and j <= j_end:
            if arr[i] < arr[j]:
                result.append(arr[i])
                i += 1
            elif arr[i] > arr[j]:
                result.append(arr[j])
                j += 1
            else:
                result.append(arr[i])
                result.append(arr[j])
                i += 1
                j += 1
        
        while i <= i_end:
            result.append(arr[i])
            i += 1
            
        while j <= j_end:
            result.append(arr[j])
            j += 1
            
        result_index = 0
        for idx in range(start, end + 1):
            arr[idx] = result[result_index]
            result_index += 1
        
        