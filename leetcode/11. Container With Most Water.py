class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        if not height:
            return 0
        if len(height) == 1:
            return 1
    
        sizeOf = 0
        right = len(height) - 1
        while (left < right):
            x = min(height[left], height[right])
            sizeOf = max(sizeOf, (x*(right- left)))
            if height[left]< height[right]:
                left += 1
            else:
                right -= 1
        return sizeOf
