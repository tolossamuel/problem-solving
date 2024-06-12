class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        left = 0
        right = 0
        
        while(left < len(name) and right < len(typed)):
            if name[left] == typed[right]:
                left += 1
            elif right == 0 and name[left] != typed[right]:
                return False
            elif typed[right-1] != typed[right] and name[left] != typed[right]:
                return False
            right +=1
            if left >= len(name):
                while(right < len(typed)):
                    if name[left-1] != typed[right]:
                        return False
                    
                    right += 1
        
        if left >= len(name):
            return True
        return False
        