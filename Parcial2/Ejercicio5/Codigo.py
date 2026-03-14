class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Paso 1: ordenar intervalos por el inicio
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # Si la lista está vacía o no hay solapamiento
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Fusionar intervalos
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged