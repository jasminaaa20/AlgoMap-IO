class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges = []
        range_start = nums[0]
        range_end = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            if current != nums[i-1] + 1:
                if range_start == range_end:
                    ranges.append(str(range_start))
                else:
                    ranges.append("{}->{}".format(range_start, range_end))
                range_start = current
                range_end = current
            else:
                range_end = current

        # Append the last range (which is missing in the original code)
        if range_start == range_end:
            ranges.append(str(range_start))
        else:
            ranges.append("{}->{}".format(range_start, range_end))
        
        return ranges
        # Time Complexity: O(n)
        # Space Complexity: O(n)
