class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        current_combo = [""]

        for digit in digits:
            new_combo = []
            for combo in current_combo:
                for char in char_map[digit]:
                    new_combo.append(combo + char)
            current_combo = new_combo

        return current_combo
