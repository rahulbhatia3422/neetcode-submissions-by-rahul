from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum_allowed: int) -> bool:
            """Check if we can split nums into <= k subarrays with each sum <= max_sum_allowed"""
            current_sum = 0
            subarrays_needed = 1  # Start with one subarray
            
            for num in nums:
                # If adding this num would exceed max_sum_allowed
                # start a new subarray
                if current_sum + num > max_sum_allowed:
                    subarrays_needed += 1
                    current_sum = num
                    # If we need more than k subarrays, it's impossible
                    if subarrays_needed > k:
                        return False
                else:
                    current_sum += num
            return True
        
        # Binary search boundaries:
        # Minimum possible answer: largest element (when k = n)
        # Maximum possible answer: sum of all elements (when k = 1)
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if can_split(mid):
                # Try for a smaller maximum sum
                right = mid
            else:
                # Need larger maximum sum
                left = mid + 1
                
        return left