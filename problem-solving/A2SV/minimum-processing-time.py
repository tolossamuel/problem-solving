class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        ans = 0
        tasks.sort(reverse = True)
        processorTime.sort()
        index = 0
        for i in range(0,len(tasks)-3,+4):
            ans = max(processorTime[index]+tasks[i],ans)
            index += 1
        return ans