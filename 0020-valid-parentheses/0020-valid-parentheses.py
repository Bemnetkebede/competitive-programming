class Solution:
    def isValid(self, s: str) -> bool:
        parentesis = {"]" : "[" , "}" : "{" , ")":"("}
        stack = []
        for i in s:
            if i in parentesis.keys():
                if not stack:
                    return False
                top_val = stack[-1]
                if top_val == parentesis[i]:
                    stack.pop()
                else:
                    return False
            else:
              stack.append(i)
        return not stack 