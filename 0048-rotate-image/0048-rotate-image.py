class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # compute size of matrix

        n = len(matrix)

        # compute squares of outer layer until the midpoint

        for i in range(n//2 + n%2):
            # for x axis, we dont need to go to the midpoint, only one step before it
            for j in range(n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp

        return matrix