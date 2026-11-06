class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
          return []

        intervals.sort(key=lambda x: x[0])  # Sort the intervals based on start time
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:  # If the current interval overlaps with the last merged interval
                merged[-1][1] = max(merged[-1][1], interval[1])  # Merge the intervals by updating the end time
            else:
                merged.append(interval)  # Add the current interval as a new merged interval

        return merged  