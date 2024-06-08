def solution(nums):
    removed = len(set(nums))
    half = len(nums) // 2
    if removed > half:
        return half
    else:
        return removed
    return answer