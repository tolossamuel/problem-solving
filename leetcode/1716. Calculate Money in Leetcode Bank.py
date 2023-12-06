# class Solution(object):
#     def totalMoney(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         def calculat(n,x):
#             if n <= x:
#                 return 0
#             else:
#                 return n+calculat(n-1,x)
      
#         ans = 0
#         x = 0
#         m = n
#         while(n >0):
#             if n >= 7:
                
#                 ans += calculat(7+x,x)
#                 x+= 1
#             else:
                
#                 ans += calculat(n+x,x)
#                 n == 0
            
#             n -= 7
           
#         return ans
a = 1234
print(str(a).count("1"))