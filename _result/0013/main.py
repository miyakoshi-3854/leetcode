class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        num = 0

        idx = 0
        while idx < len(s):
            two_symbol = s[idx : idx + 2]
            if two_symbol in roman_value:
                num += roman_value[two_symbol]
                idx += 2
            elif s[idx] in roman_value:
                num += roman_value[s[idx]]
                idx += 1

        return num
