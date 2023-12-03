# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         """
#         :type asteroids: List[int]
#         :rtype: List[int]
#         """
#         stack = [asteroids[0]]
#         for i in range(1,len(asteroids)):
           
#             if not stack:
#                 stack.append(asteroids[i])
#             elif abs(stack[-1] + asteroids[i]) > (max(abs(stack[-1]),abs(asteroids[i]))):
               
#                 stack.append(asteroids[i])
       
                
            
#             elif stack[-1] < 0:
#                 stack.append(asteroids[i])
#             else:
#                 print(stack)
#                 while(stack[-1] <= abs(asteroids[i])):
#                     if stack:
#                         if (stack[-1]*-1) == (asteroids[i]):

#                             stack.pop()
#                             break
#                         if abs(stack[-1] + asteroids[i]) > (max(abs(stack[-1]),abs(asteroids[i]))):
                            
#                             stack.append(asteroids[i])
#                             break
#                         stack.pop()
                        
#                         if not stack:
#                             stack.append(asteroids[i])
#                             break
#                     elif not stack:
#                         stack.append(asteroids[i])
#                         break
#         return stack



        
                    
n = "["
if n.isdigit():
	print(True)

                    