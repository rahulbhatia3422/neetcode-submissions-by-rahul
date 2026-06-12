from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        
        if max(matchsticks) > target:
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        
        def backtrack(index):
            if index == len(matchsticks):
                return True
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                    
                    # KEY OPTIMIZATION: If this side was empty and failed,
                    # skip other empty sides (they're identical)
                    if sides[i] == 0:
                        break
            
            return False
        
        return backtrack(0)