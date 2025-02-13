class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If merged is empty or current interval doesn't overlap with the last one
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge by updating the end of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
