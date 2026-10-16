class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        pass

        nums.sort()
        count = 0
        
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                target = nums[i-1] + 1
                count += target - nums[i]
                nums[i] = target
        return count

