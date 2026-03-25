from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # "."はany char、"*"は直前の文字の繰り返しを許容
        
        @lru_cache
        def matches(s_idx, p_idx):

            if p_idx == len(p):
                return s_idx == len(s)

            in_bounds = s_idx < len(s)
            char_match = in_bounds and (s[s_idx] == p[p_idx] or p[p_idx] == ".")

            if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                skip_star = matches(s_idx, p_idx + 2)
                use_star = char_match and matches(s_idx + 1, p_idx)
                return skip_star or use_star

            return char_match and matches(s_idx + 1, p_idx + 1)
        
        return matches(0, 0)