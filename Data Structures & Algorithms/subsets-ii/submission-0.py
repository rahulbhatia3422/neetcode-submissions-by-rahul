from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_idx = 0  # Track where previous duplicates started adding

        for i in range(len(nums)):
            # If current number equals previous number, start from previous start index
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)  # Store current length before adding new subsets
            
            # Add current number to subsets from idx to prev_idx
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res