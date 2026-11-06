class Solution:
    def removeOuterParentheses(self, s: str) -> str:
                stack = []
                res = []
                for i in s:
                    if i == "(":
                        if stack:
                            res.append(i)
                        stack.append(i)
                    else:
                        stack.pop()
                        if stack:
                            res.append(i)
                return ''.join(res)