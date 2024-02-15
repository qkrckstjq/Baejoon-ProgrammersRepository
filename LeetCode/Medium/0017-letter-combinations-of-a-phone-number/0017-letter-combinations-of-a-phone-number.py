base = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        input_digit = list(digits)
        stack = []
        result = []

        for start_c in base[input_digit[0]]:
            stack.append(start_c[0])

        while stack:
            cur_str = stack.pop()

            if len(cur_str) == len(input_digit):
                result.append(cur_str)
                continue

            for cur_c in base[input_digit[len(cur_str)]]:
                next_str = cur_str
                next_str += cur_c
                stack.append(next_str)

        return result