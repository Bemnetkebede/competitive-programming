class Solution:
    def reverseParentheses(self, s: str) -> str:
            stack = []
            pairs = {}
            
            for i, c in enumerate(s):
                if c == '(':
                    stack.append(i)
                elif c == ')':
                    j = stack.pop()
                    pairs[i], pairs[j] = j, i
            
            result = []
            step = 1
            i = 0
            while i < len(s):
                if s[i] in '()':
                    i = pairs[i]
                    step = -step
                else:
                    result.append(s[i])
                i += step
            
            return ''.join(result)