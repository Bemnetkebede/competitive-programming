class Solution(object):
    def percentageLetter(self, s, letter):
        l = len(s)
        count = 0
        for i in  s:
            if i == letter:
                count += 1
        return (count*100//l)
    