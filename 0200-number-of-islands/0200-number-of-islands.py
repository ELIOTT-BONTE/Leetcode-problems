class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go trough matrix
        # when encountering 1
        # call flood
        # increment count by 1

        # flood
        # if square = 1
        # replace it by 0
        # call flood on neighbours, if within boundaries
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0

        def flood(x,y):
            if grid[x][y] == "1":
                grid[x][y] = "0"
                for dx, dy in directions:
                    if 0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0]):
                        flood(dx + x, dy + y)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    count += 1
                    flood(x,y)

        return count                    
