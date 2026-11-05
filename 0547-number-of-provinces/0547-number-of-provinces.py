class Solution(object):
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        numberOfComponents = 0
        visit = [False] * size

        for i in range(size):
            if not visit[i]:
                numberOfComponents += 1
                self.dfs(i, isConnected, visit)

        return numberOfComponents
    # def findCircleNum(self, isConnected):
    #     res = 0 
    #     n = len(isConnected)
    #     for i in range(n):
    #         res += sum(isConnected[i])
    #     print(res//2)



        # res = 0
        # itself = 0
        # other = 0
        # n = len(isConnected)
        # for i in range(n):
        #     for j in range(len(isConnected[i])):
        #         if i == j and isConnected[i][j] == 1:
        #             itself += 1
        #         elif isConnected[i][j] == 1 and i != j :
        #             other += 1
        # print(itself , other)
        # if other > 0:
        #     return other
        # else:
        #     return itself
        
        