class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for file in logs:
            print(stack)
            print(file)
            if file == '../':
                if stack:
                  stack.pop()
            elif file == './':
                pass
            else:
                stack.append(file)
        return len(stack)