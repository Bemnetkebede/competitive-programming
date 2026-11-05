class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ## Bubble sorting
        # for i in range(len(heights)):
        #     for i in range(len(names)-i-1):
        #         if heights[i] < heights[i + 1]:
        #             heights[i] , heights[i+1] = heights[i +1] , heights[i]
        #             names[i] , names[i+1] = names[i+1] , names[i]
        # return names
        

        ## selected sorting
        # for j in range(len(heights)):
        #     min_idx = j
        #     for i in range(j+ 1 , len(heights)):
        #         if heights[min_idx] < heights[i]:
        #             heights[min_idx] , heights[i] =  heights[i] ,heights[min_idx]
        #             names[min_idx] , names[i] = names[i] , names[min_idx] 
        # return names
        ## insertion sort
        # for x in range(1 , len(heights)):
        #     i = x
        #     j = i - 1
        #     while j >= 0 :
        #         if heights[i] > heights[j]:
        #             heights[i] , heights[j] = heights[j] , heights[i]
        #             names[i] , names[j] = names[j] , names[i]
        #             i = j
        #             j -= 1 
        #         else:
        #             j -= 1 
        # return names


        ## counting sort
        arr = arr = [0] * (max(heights) + 1)
        for idx ,val in enumerate(heights):
            arr[heights[idx]] = (names[idx] , val)
        res = []
        for j in arr:
            if isinstance(j, tuple) and j[1] > 0:
                res.append(j[0])
        return res[::-1]



         