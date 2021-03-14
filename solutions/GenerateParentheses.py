from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
            if left < n:
                generate(s + '(', left + 1, right)
            if left > right:
                generate(s + ')', left, right + 1)

        generate()
        return res

print(Solution().generateParenthesis(3))

