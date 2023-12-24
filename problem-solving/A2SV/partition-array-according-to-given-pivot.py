class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        p = 0
        for i in range(len(nums),0,-1):
            if nums[i-1] == pivot:
                p = i-1
                break
        left = p-1
        right = p+1
        equal = 0
        while(left >= 0 or right < len(nums)):
            
            if left >= 0:
                
                if nums[left] > nums[p]:
                    
                    nums.insert(p+1, nums[left])  
                                    
                    nums.pop(left)
                    p-= 1
                elif nums[left] == nums[p]:
                    equal += 1
                    nums.insert(p,nums[left])
                    nums.pop(left)
            if right < len(nums):
                if nums[right] < nums[p]:
                    nums.insert(p-equal,nums[right])
                    nums.pop(right+1)
                    p += 1
                elif nums[right] == nums[p]:
                    nums.insert(p,nums[right])
                    nums.pop(right+1)
                    equal += 1
                    p+=1  
            left -= 1
            right +=1
         
        return nums
