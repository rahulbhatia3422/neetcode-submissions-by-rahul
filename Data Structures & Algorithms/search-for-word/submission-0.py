class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or row >= m or col < 0 or col >= n or
                (row, col) in visited or board[row][col] != word[index]):
                return False
            
            visited.add((row, col))
            
            found = (dfs(row + 1, col, index + 1) or
                    dfs(row - 1, col, index + 1) or
                    dfs(row, col + 1, index + 1) or
                    dfs(row, col - 1, index + 1))
            
            visited.remove((row, col))
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False