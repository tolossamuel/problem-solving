# class Solution(object):
#     def deckRevealedIncreasing(self, deck):
#         """
#         :type deck: List[int]
#         :rtype: List[int]
#         """
#         n = len(deck)
#         deck.sort()
#         result = [0] * n
#         indexs = deque(range(n))
#         for card in deck:
#             result[indexs.popleft()] = card
#             if indexs:
#                 indexs.append(indexs.popleft())
#         return result

def happy(n,b,arr):
            if n == 1:
                
                return True
            elif n <= 3:
               
                return False
            else:
                m = str(n)
                sumOf = 0
                for i in range(len(m)):
                    sumOf += int(m[i])**2
                print(sumOf)
                
                
                if  sumOf in arr:
                    print(sumOf,n,b)
                    print(True)
                    checker = True
                    
                    return False
                else:
                    arr.append(sumOf)
                  
                    return happy(sumOf,b,arr)

name = happy(5,5,[])
print(name)