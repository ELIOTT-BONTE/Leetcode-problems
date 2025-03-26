from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        #intialize zeroes to 0
        #rest at infinity
        #at each non zero, add to queue
        # consume queue by spreading to adjacent cells (val + 1), if within boundaries

        width = len(mat)
        length = len(mat[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x in range(width):
            for y in range(length):
                if mat[x][y] == 0:
                    queue.append([x,y])
                elif mat[x][y] == 1:
                    mat[x][y] = float("inf")


        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_y = y + dy
                new_x = x + dx
                if 0 <= new_y < length and 0 <= new_x < width and mat[x][y] + 1 < mat[new_x][new_y]:
                    mat[new_x][new_y] = mat[x][y] + 1
                    queue.append([new_x, new_y])
        
        return mat