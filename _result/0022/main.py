class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open_count, close_count):
            if len(current) == n * 2:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if open_count > close_count:
                backtrack(current + ")", open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)
        return result
