class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def fill(x,y, original):
            if image[x][y] == color:
                return
            else:
                image[x][y] = color
                for dx, dy in directions:
                    if 0 <= dx + x < len(image) and 0 <= dy + y < len(image[0]) and image[dx + x][dy + y] == original:
                        fill(dx + x, dy + y, original)

        original_color = image[sr][sc]
            
        fill(sr, sc, original_color)

        return image