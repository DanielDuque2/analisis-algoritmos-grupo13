class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not s or s[0] == '0':
            return 0

        vector_posiciones = [0] * (n + 1)
        vector_posiciones[0] = 1
        vector_posiciones[1] = 1

        for i in range(2, n + 1):
            digito = int(s[i-1])
            digitos = int(s[i-2:i])

            if digito >= 1:
                vector_posiciones[i] += vector_posiciones[i-1]

            if 10 <= digitos <= 26:
                vector_posiciones[i] += vector_posiciones[i-2]

        return vector_posiciones[n]