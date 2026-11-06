class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        cur_sum = 0
        for i in gain:
            cur_sum += i
            highest = max(highest , cur_sum)
        return highest
