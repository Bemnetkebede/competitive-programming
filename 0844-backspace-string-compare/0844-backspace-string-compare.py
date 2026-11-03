class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(s):
            stack = []
            for i in s:
                if i == '#' and stack:
                    stack.pop()
                elif i == '#' and not stack:
                    pass
                else:
                    stack.append(i)   
            return stack 
        return build_string(s) == build_string(t) 