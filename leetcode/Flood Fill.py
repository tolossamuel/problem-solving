class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        starting_point = image[sr][sc]
        self.dfs_search(image, sr, sc, color, starting_point)
        return image

    def dfs_search(self,image, sr, sc, color, starting_point):
        if (sr<0 or sr>len(image)-1 or sc<0 or sc>len(image[0])-1 or image[sr][sc] != starting_point or image[sr][sc] == color) :
            return 
        image[sr][sc] = color
        self.dfs_search(image, sr, sc+1, color, starting_point)
        self.dfs_search(image, sr+1, sc, color, starting_point)
        self.dfs_search(image, sr, sc-1, color, starting_point)
        self.dfs_search(image, sr-1, sc, color, starting_point)
        