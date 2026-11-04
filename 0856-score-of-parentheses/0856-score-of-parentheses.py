class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] 
        
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                val = stack.pop()
                
                calculated_score = val * 2 if val > 0 else 1
                
                stack[-1] += calculated_score
            
        return stack[0]
