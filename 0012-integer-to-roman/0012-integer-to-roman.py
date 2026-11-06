class Solution:
    def intToRoman(self, num: int) -> str:
         # Create a dictionary to store the mapping of place values to Roman numerals
        roman_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        
        roman_numeral = ''
        for value, numeral in roman_map.items():
            while num >= value:
                roman_numeral += numeral
                num -= value

        return roman_numeral