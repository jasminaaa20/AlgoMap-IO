class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        start = nums[0]  # Track start of the current range

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # If discontinuity found
                ranges.append(str(start) if start == nums[i - 1] else f"{start}->{nums[i - 1]}")
                start = nums[i]  # Start new range

        # Append the last range (merged into loop logic)
        ranges.append(str(start) if start == nums[-1] else f"{start}->{nums[-1]}")
        
        return ranges
        # Time Complexity: O(n)
        # Space Complexity: O(n)
