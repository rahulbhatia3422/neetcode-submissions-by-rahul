from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        res = 0
        
        for r in range(m):

            for c in range(n):
                
                if grid[r][c] == 1:
                    res += 4  # Assume all 4 sides are exposed
                    
                    # Check cell above
                    if r > 0 and grid[r-1][c] == 1:
                        res -= 2  # Remove shared vertical edge
                    
                    # Check cell to the left
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2  # Remove shared horizontal edge
        
        return res