class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num))-2
        print(length,bin(num))
        max_num = (2**length)-1
        return max_num^num