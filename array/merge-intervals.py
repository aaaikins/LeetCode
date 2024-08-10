class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        merge = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = merge[-1][1]
            if start <= lastEnd:
                merge[-1][1] = max(end, lastEnd)
            else:
                merge.append([start, end])

        return merge

        