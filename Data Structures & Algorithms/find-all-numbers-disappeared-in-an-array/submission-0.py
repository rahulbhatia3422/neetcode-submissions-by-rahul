class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark existing numbers
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # Collect missing numbers
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]