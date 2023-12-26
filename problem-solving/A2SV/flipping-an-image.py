class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i] = image[i][::-1]
        print(image)
        for i in range(len(image)):
            for y in range(len(image[i])) :
                if image[i][y] == 1:
                    image[i][y] = 0
                else:
                    image[i][y] = 1
        return image
        