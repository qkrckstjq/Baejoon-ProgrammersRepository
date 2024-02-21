class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        left = 0
        right = len(numbers) - 1
        while True:
            mid = (left + right) // 2
            if numbers[i] + numbers[mid] == target and i != mid:
                return [i + 1, mid + 1]
            if numbers[mid] <= target - numbers[i]:
                left = mid + 1
            elif numbers[mid] > target - numbers[i]:
                right = mid - 1
            if left > right:
                i += 1
                left = i
                right = len(numbers) - 1