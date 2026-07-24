import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: if the grid is empty, there are no islands
        if not grid:
            return 0
            
        # Get the matrix dimensions
        rows, cols = len(grid), len(grid[0])
        # A set to keep track of already visited coordinates (r, c)
        visit = set()
        islands = 0

        # Helper function to perform BFS and mark the entire island as visited
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                # Define 4-directional movements: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    
                    # Check if the neighboring cell is:
                    # 1. Within the grid boundaries
                    # 2. Land ("1")
                    # 3. Not already visited
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visit):
                        
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c)) # Mark it visited immediately to avoid duplicate queueing

        # Main loops to iterate through every single cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find unvisited land, it represents a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c) # Trigger BFS to map out and visit the entire island
                    islands += 1 # Increment our island counter
                    
        return islands