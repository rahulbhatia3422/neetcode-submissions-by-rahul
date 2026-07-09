class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We should use a hash map to store numbers we’ve seen and their indices.
        # Beacuse if array is not sorted then also it will work fine

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []