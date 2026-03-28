class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        
        # Si la suma es impar, no se puede dividir en dos partes iguales
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[i] = True si se puede formar suma i
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # recorrer hacia atrás
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
    
    # DP 1D: dp[i] indica si es posible formar suma i
    # Complejidad: O(n * target) tiempo, O(target) espacio