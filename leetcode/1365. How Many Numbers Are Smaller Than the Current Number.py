class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [8,1,2,2,3]
        # for 8 their is [1,2,2,3]
        # for 1 their is no any numbers less than it
        #  for 2 [1], for 2 [1] for 3 [ 1,2,2]
    #     nested for loop with out considering time complexity and efficiency 
    #    # [8,1,2,2,3]
    #    we take 8 and iterate all the elements in the array we declare counter variable to count the number of small elements form 8 
    #    and append it on the new array
    #    time complexity is O(n^2) space O(n) because we are using array
        # counter = 0
        # result = []
        # for i in range(len(nums)):
        #     for y in range(len(nums)):
        #         if nums[i] > nums[y]:
        #             counter += 1
        #     result.append(counter)
        #     counter = 0
        # return result
        list1 = list(nums)
        list1.sort()
        dic = {}
        for i in range(len(list1)):
            try:
                
                if dic[list1[i]]:
                    print(1234)
                    continue
            except:
                dic[list1[i]] = i
        print(dic)
        for i in range(len(nums)):
            list1[i] = dic[nums[i]]
        return list1


        return list1
        