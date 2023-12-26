class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        check = False
        stack = [0,0]
        for i in range(len(arr)):
            if arr[i] > stack[0]:
                stack = [arr[i],i]
        if stack[1] == 0 or stack[1] == len(arr)-1:
            return False
        left = stack[1]-1
        right = stack[1]+1
       
        while(left >= -1 and right <= len(arr)):
            if left >= 0:
                if arr[left] >= arr[left+1]:
                    return False
                else:
                    left -= 1
            if right < len(arr):
                if arr[right] >=  arr[right-1]:
                
                    return False
                else:
                    right += 1
            if left == -1 and right == len(arr):
                break

        return True


        