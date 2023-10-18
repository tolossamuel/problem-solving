class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        counter = 0
        for i in range(len(logs)):
            if (logs[i] == "../"):
                if(counter -1 >=0):
                    counter -= 1
            elif (logs[i] != "./"):
            
                counter += 1
        return counter
            