class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = merge[-1][1]

            if start <= lastEnd:
                merge[-1][1] = max(lastEnd, end)
            else:
                merge.append([start, end])

        return merge

        