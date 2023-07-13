class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        sub_string_length = []
        y=0
        i=0
        while(y!=len(s)):
            while(i!=len(s)):
                if  s[i]  in  sub_string:
                    sub_string_length.append(len(sub_string))
                    sub_string = ""
                    break
                    
                else:
                    sub_string += s[i]
                i+=1
            y+=1
            if i<len(s):
                  i=y
        sub_string_length.append(len(sub_string))
        if " " in s:
            sub_string_length.append(1)
        if sub_string_length:
            longest_substring = max(sub_string_length)
        else:
            longest_substring = 0
        return longest_substring