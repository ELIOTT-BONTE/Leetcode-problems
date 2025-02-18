class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(0,-1),(-1,0),(0,1)]
        original_color = image[sr][sc] 


        if color == original_color:
            return image
        
        def colorize(r, c):
            if r < 0 or r > len(image)-1 or c < 0 or c > len(image[0])-1 or image[r][c] == color:
                pass
            elif image[r][c] == original_color :
                image[r][c] = color
                for d in directions:
                    colorize(r+d[0], c+d[1])

        colorize(sr, sc)

        return image