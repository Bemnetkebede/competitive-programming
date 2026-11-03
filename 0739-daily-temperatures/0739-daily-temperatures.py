class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]: 
                stackIdx , stackVal = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([i , temperatures[i]])
        return res    