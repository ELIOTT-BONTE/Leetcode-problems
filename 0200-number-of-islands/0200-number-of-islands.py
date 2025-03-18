class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        counter = 0
        directions = [[1,0],[-1,0], [0,-1],[0,1]]
        queue = deque()

        def clearIsland(x, y):
            grid[x][y] = "0"
            for dx, dy in directions:
                newx = dx+x
                newy = dy+y
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy] == "1":
                    clearIsland(newx,newy)

        for x in range(len(grid)) :
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    counter +=1
                    clearIsland(x,y)

        return counter


        #iterate through the map
        #when meeting a 1, increase counter and clear island
    
        #when done iterating, return counter

