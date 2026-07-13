from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node: int, parent: int) -> int:
            # Time needed for this subtree
            time = 0
            
            for child in adj[node]:
                if child != parent:
                    child_time = dfs(child, node)
                    if child_time > 0 or hasApple[child]:
                        # Need to traverse edge to child (2 units)
                        # Plus the time needed inside child's subtree
                        time += 2 + child_time
            
            return time
        
        return dfs(0, -1)