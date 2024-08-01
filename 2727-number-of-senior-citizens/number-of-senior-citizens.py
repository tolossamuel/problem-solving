class Solution:
    def countSeniors(self, details: List[str]) -> int:
        _sum = 0
        for x in details:
            _sum +=1 if  int(x[-4:-2]) > 60 else 0
        return _sum
        