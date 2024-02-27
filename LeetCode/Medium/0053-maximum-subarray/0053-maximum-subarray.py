class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def cut_first(nums):
            for i in range(0, len(nums), 1):
                if nums[i] > 0:
                    return i
            return -1

        def cut_last(nums):
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > 0:
                    return i

            return -1

        def get_max_subarray(front_i, last_i):
            if front_i == -1 and last_i == -1:
                return max(nums)

            total = 0
            sum_total = []
            for num in nums[front_i:last_i + 1]:
                if total + num > 0:
                    total += num
                    sum_total.append(total)

                else:
                    total = 0

            return max(sum_total)

        front_i = cut_first(nums)
        last_i = cut_last(nums)
        return get_max_subarray(front_i, last_i)