class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        nino = 0
        galleta = 0

        while nino < len(g) and galleta < len(s):
            if s[galleta] >= g[nino]:
                nino += 1
            galleta += 1

        return nino