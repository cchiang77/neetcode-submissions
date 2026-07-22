class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        fresh_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        minutes = 0
        while queue and fresh_oranges > 0:
    
            for i in range(len(queue)):
                r, c = queue.popleft()
                deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for delta in deltas:
                    dr, dc = delta
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append([nr, nc])
                        fresh_oranges -= 1
            minutes += 1
        
        return minutes if fresh_oranges == 0 else -1
