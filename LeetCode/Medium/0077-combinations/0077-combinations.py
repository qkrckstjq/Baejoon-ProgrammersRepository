class Solution:
    from itertools import combinations
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations([x for x in range(1,n+1)],k))