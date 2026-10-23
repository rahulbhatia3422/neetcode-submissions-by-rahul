class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        arr = sorted(set(nums))

        left = 0
        max_keep = 0

        for right in range(len(arr)):

            while arr[right] - arr[left] >= n:
                left += 1

            max_keep = max(max_keep, right - left + 1)

        return n - max_keep