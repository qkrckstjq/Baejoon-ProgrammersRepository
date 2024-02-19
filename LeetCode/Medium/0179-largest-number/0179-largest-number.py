class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.merge_sort(nums, 0, len(nums) - 1)
        if self.get_one(nums[0], 0) == 0:
            return '0'
        return ''.join(map(str, nums))
        
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
            if self.compare(arr[i], arr[j]):
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j += 1
        while i <= i_end:
            result.append(arr[i])
            i += 1
        while j <= j_end:
            result.append(arr[j])
            j += 1
        result_index = 0
        for i in range(start, end + 1):
            arr[i] = result[result_index]
            result_index += 1
            
    def get_one(self, num, index):
        return int(list(str(num))[index])
    
    def compare(self, num1, num2):
        #True면 num1이 더 큼, false면 반대
        num1_first = self.get_one(num1, 0)
        num2_first = self.get_one(num2, 0)
        num1_list = list(map(int, str(num1)))
        num2_list = list(map(int, str(num2)))
        if num1_first > num2_first:
            return True
        elif num1_first < num2_first:
            return False
        else:
            return self.if_same(num1_list, num2_list)

    def if_same(self, num1_list, num2_list):
        i, j = 0, 0
        same_count = 1
        while i < len(num1_list) or j < len(num2_list):
            i = (i + 1) % len(num1_list)
            j = (j + 1) % len(num2_list)
            digit1 = num1_list[i]
            digit2 = num2_list[j]
            if digit1 > digit2:
                return True
            elif digit1 < digit2:
                return False
            else:
                same_count += 1
                if same_count > 100:
                    return False
        return True
        