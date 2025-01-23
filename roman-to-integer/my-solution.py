class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = symbol_values[s[-1]]
        length = len(s)
        i = length - 2

        while i >= 0:
            if symbol_values[s[i]] < symbol_values[s[i+1]]:
                sum -= symbol_values[s[i]]
            else:
                sum += symbol_values[s[i]]
            i -= 1
        
        return sum
            
