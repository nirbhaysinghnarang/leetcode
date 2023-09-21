from collections import defaultdict

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        if not pressedKeys:
            return 0
        
        hm = {
            "2": ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        inverted = defaultdict(str)
        for key, letters in hm.items():
            for i, letter in enumerate(letters):
                inverted[(i + 1) * key] = letter

        def genCombs(index, memo):
            if index == len(pressedKeys):
                return 1

            if index in memo:
                return memo[index]

            max_end = min(index + 5, len(pressedKeys))
            combinations = 0

            for x in range(index, max_end):
                nums = str(pressedKeys[index:x + 1])
                if nums in inverted:
                    combinations += genCombs(x + 1, memo)

            memo[index] = combinations
            return combinations

        memo = {}
        return genCombs(0, memo) % (10 ** 9 + 7)
