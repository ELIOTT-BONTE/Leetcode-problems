class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse grid
        # each time island is encountered, flood it
        # to flood, use BFS with queue
        # return number of times flood was called

        count = 0
        height = len(grid)
        width = len(grid[0])

        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        def flood(x,y):
            
            queue = deque([(x,y)])
            while queue:
                x, y = queue.popleft()
                for directionX, directionY in directions:
                    newX = x + directionX
                    newY = y + directionY
                    if (0 <= newX < height) and (0 <= newY < width) and grid[newX][newY] == "1":
                        grid[newX][newY] = "0"
                        queue.append((newX, newY))



        for x in range(height):
            for y in range(width):
                if grid[x][y] == "1":
                    flood(x,y)
                    count += 1





        return count