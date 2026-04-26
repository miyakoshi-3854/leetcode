class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(min(strs, key=len))):
            all_chars_match = [s[i] == strs[0][i] for s in strs]
            if all(all_chars_match):
                prefix += strs[0][i]
            else:
                return prefix

        return prefix


if __name__ == "__main__":
    s = Solution()
    s.solve()
