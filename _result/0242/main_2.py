class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            char_count[char] += 1

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

        for value in char_count.values():
            if value != 0:
                return False

        return True
