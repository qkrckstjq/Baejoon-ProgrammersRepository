class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            return_value = 1
            for i in range(1, n + 1, 1):
                return_value *= i

            return return_value

        def combination(n, r):
            mid_v = factorial(n) / factorial(n - r)
            return mid_v / factorial(r)

        a = n
        b = 0
        total = 0
        while a >= b:
            total += combination(a, b)
            a -= 1
            b += 1

        return int(total)