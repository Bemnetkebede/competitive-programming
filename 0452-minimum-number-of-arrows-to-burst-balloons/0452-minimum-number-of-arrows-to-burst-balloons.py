class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        shout = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                shout += 1
                end = points[i][1]
            else:
                if end >  points[i][1]:
                    end = points[i][1]
                
        return shout
                


        
        