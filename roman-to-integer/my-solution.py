class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum = symbol_values[s[-1]]

        index = len(s) - 2

        while index >= 0:
            current_value = symbol_values[s[index]]
            proceeding_value = symbol_values[s[index+1]]

            if current_value < proceeding_value:
                sum -= current_value
            else:
                sum+= current_value
            index -= 1
        
        return sum
        # Time complexity: O(n)
        # Space complexity: O(1)
        
