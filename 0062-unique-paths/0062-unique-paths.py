class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[0]*n]*m
        print(mat)

        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0:
                    mat[x][y] = 1
                else:
                    mat[x][y] = mat[x-1][y] + mat[x][y-1]
        
        return mat[m-1][n-1]