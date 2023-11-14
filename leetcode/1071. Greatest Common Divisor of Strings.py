class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        s1 = max(str1, str2, key = lambda x: len(x))
        if s1 == str1:
            s2 = str2
        else:
            s2 = str1
        a1, a2 = len(s1), len(s2)

        if s2 * (a1//a2) == s1:
            return s2
        
        for i in range(2, a2//2 + 1):
            if (a2 / i) % 1 == 0:
                if s2[:a2//i]*i == s2:
                    if s1[:a2//i]*int(i*a1/a2) == s1:
                        if s2[:a2//i] == s1[:a2//i]:
                            return s2[:a2//i] 

        if s1.count(s1[0]) == a1:
            if s2.count(s2[0]) == a2:
                if s1[0] == s2[0]:
                    return s1[0]

        return ''