class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.robLine(nums[1:]),   # Skip first house
            self.robLine(nums[:-1])   # Skip last house
        )

    def robLine(self, houses):
        prev2 = 0   # Max money up to house i-2
        prev1 = 0   # Max money up to house i-1

        for money in houses:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1