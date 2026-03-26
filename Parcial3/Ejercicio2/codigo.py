class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)  # O(1) búsqueda
        dp = [False] * (len(s) + 1)
        dp[0] = True  # string vacío es válido

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # ya encontramos una forma válida

        return dp[len(s)]