class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    continue
                
                path.append(nums[i])
                backtrack(i, path, remaining - nums[i])
                path.pop()
    
        result = []
        nums.sort()
        backtrack(0, [], target)
        return result
        