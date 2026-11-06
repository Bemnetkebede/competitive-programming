class Solution(object):
    def sumOfThree(self, num):
        x = (num - 3) % 3
        if x == 0:
            x = (num - 3) / 3
            return [ x , x+1 , x+2]
        return []
          

