class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        while(left <= right):

            middle = (left + right)//2
            if letters[middle] > target and letters[middle - 1 ] <= target:
                return letters[middle]
            
            elif (letters[middle]) > target:
                right = middle -1 
            elif (letters[middle] <= target):
                left = middle+1
        return letters[0]