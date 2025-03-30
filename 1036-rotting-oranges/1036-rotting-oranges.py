from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        minutes = 0
        #count fresh oranges
        #add roten ones to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c, 0])


        #while there is a queue,
        #spread rot to neighbours and add a minute

        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                if 0 <= dr + r < rows and 0 <= dc + c < cols and grid[dr+r][dc+c] == 1:
                    grid[dr+r][dc+c] = 2
                    fresh -= 1
                    print(f"appended {dr+r},{dc+c} to the queue")
                    queue.append([dr+r, dc+c, minutes+1])

        return minutes if fresh ==0 else -1

        #if no more fresh oranges, return minutes
        #if no more queue and still fresh oranges, return -1