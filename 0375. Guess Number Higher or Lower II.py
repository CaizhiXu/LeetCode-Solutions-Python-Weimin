# method 2: dp
# time O(n^3), space O(n^2)
class Solution(object):
    def getMoneyAmount(self, n):
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        # dp[i][i+1] must be zero, so length==1 is skipped
        for length in range(2, n+1):
            for i in range(1, n+2-length):
                j = i + length - 1
                dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1])
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        
        return dp[1][n]


# method 1: recursion with memo, time O(n^3), space O(n^2)
class Solution1(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.getMoneyAmountHelper(1, n)
    
    def getMoneyAmountHelper(self, low, high):
        if high <= low:
            return 0
        if high - low == 1:
            return low
        if high - low == 2:
            return low + 1
        
        if (low, high) in self.memo:
            return self.memo[(low, high)]
        
        min_money = float('inf')
        for num in range(low, high+1):
            min_money = min(min_money, 
                            num + max(self.getMoneyAmountHelper(low, num-1), 
                                      self.getMoneyAmountHelper(num+1, high)))
        
        self.memo[(low, high)] = min_money
        return min_money
    
