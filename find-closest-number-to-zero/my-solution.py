class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_number = 100001

        for num in nums:
            if abs(num) < abs(closest_number) or (abs(num) == abs(closest_number) and num > closest_number):
                closest_number = num
        
        return closest_number
        # Time complexity: O(n)
        # Space complexity: O(1)
