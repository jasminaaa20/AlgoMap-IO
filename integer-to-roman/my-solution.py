class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define a list of tuples mapping Roman numerals to their integer values
        roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = []
        for value, symbol in roman_map:
            # While the number is greater than or equal to the value
            while num >= value:
                result.append(symbol)  # Append the Roman numeral to the result
                num -= value  # Subtract the value from the number
        return ''.join(result)
