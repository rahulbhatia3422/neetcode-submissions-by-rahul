class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp array for the first row
        dp = [1] * n
        
        # Process each row
        for i in range(1, m):
            # Process each column in current row
            for j in range(1, n):
                # dp[j] is from above (previous value at j)
                # dp[j-1] is from left (updated value in current row)
                dp[j] = dp[j] + dp[j-1]
        
        # Last element contains the answer
        return dp[-1]
        