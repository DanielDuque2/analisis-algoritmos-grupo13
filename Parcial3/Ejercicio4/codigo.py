class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        vector_posiciones = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    vector_posiciones[i][j] = vector_posiciones[i-1][j-1] + 1
                else:
                    vector_posiciones[i][j] = max(vector_posiciones[i-1][j], vector_posiciones[i][j-1])

        return vector_posiciones[m][n]
        