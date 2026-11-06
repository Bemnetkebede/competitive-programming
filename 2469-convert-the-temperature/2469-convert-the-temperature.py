class Solution(object):
    def convertTemperature(self, celsius):
        fer =  celsius * 1.80 + 32.00
        kel =  celsius + 273.15
        return [kel , fer]