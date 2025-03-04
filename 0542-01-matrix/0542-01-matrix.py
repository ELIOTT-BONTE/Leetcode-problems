from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for c in range(cols):
            for r in range(rows):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float("inf")

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat