def flip_and_sort():
    global arr
    n = len(arr)
    steps = []
    
    while arr != sorted(arr,reverse=True):
        if arr[0] != 1:
               for i in range(n):
                            if arr[:i+1] == sorted(arr[:i+1]) or arr[:i+1] == sorted(arr[:i+1], reverse=True):
                                    continue
                            else:
                                    arr = arr[i-1::-1]+arr[i:]
                                    steps.append(i) 
                                    break 
        else:
               steps.append(len(arr))
               arr= arr[::-1]
               print(12)            
    return steps

# Test the function
global arr
arr = [1,3,2,4]
sorting_steps = []
if(arr != sorted(arr)):
       sorting_steps = flip_and_sort()
if arr != sorted(arr):
    sorting_steps.append(len(arr))

print(sorting_steps)
