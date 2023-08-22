class Solution:
    def isPalindrome(self, s: str) -> bool:
        check=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                check+=s[i]
        check=check.lower()
        if check==check[::-1]:
            return True
        else:
            return False