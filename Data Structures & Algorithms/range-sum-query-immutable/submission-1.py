from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Build prefix sum array where prefix[i] = sum of nums[0..i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right = prefix[right+1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]