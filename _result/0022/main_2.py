class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open_count, close_count):
            if len(current) == n * 2:
                result.append("".join(current))
                return
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()
            if open_count > close_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        result = []
        backtrack([], 0, 0)
        return result