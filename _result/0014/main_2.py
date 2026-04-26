class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                result.append(chars[0])
            else:
                break
        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    s.solve()
