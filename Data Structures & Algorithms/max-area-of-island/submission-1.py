from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get grid dimensions
        m, n = len(grid), len(grid[0])
        
        # DFS to calculate island area
        def dfs(i: int, j: int) -> int:
            # Check bounds and if cell is land
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0  # Mark as visited
                # Count current cell + 4 directions
                return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1)
            return 0  # Water or out of bounds
        
        # Find maximum island area
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:  # Found land
                    max_area = max(max_area, dfs(i, j))
        
        return max_area