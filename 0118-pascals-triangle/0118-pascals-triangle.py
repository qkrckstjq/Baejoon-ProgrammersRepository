class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for i in range(1, numRows):
            prev = result[i - 1]
            temp = []
            prev_len = len(prev)
            for j in range(i + 1):
                temp.append((prev[j - 1] if j > 0 else 0) + (prev[j] if j < prev_len else 0))
            result.append(temp)
        # print(result)
        return result
