class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        removidos = 0
        ultimo = intervals[0][1]

        for i in range(1, len(intervals)):
            comienzo, final = intervals[i]

            if comienzo < ultimo:
                removidos += 1
            else:
                ultimo = final

        return removidos