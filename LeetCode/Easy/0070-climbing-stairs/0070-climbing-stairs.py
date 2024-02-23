class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]
        memo.append(1)
        memo.append(2)
        for i in range(3, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]
        