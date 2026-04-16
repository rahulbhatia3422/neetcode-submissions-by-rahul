class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Early termination checks
        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 != 0:
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # Handle case when subset_sum is negative
        if subset_sum < 0:
            return 0
        
        # DP array for subset sum count
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            # Traverse backwards to prevent using same element multiple times
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]