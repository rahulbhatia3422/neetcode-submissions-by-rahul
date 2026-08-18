class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Step 1: Sort to handle duplicates
        res = []
        
        def backtrack(start, path, current_sum):
            if current_sum == target:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Prune branch if sum exceeds target
                if current_sum + candidates[i] > target:
                    break  # sorted array → all next numbers will be larger
                
                # Choose candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, path, current_sum + candidates[i])
                # Undo choice
                path.pop()
        
        backtrack(0, [], 0)
        return res