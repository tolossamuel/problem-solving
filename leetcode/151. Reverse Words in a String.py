class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        word = list(s.split(" "))
        word = word[::-1]
       
        i = 0
        while(i + 1 < len(word)):
            if word[i] == '':
                # print("true")
                word.pop(i)
                i -= 1
            else:
                i += 1
        # print(word)
        word = " ".join(word)
        return word