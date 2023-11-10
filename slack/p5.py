tokens = ["4","13","5","/","+"]
sumof = 0
stack = []
stack2 = []
def result1 ( name,  num,  num1):
	if name == "+":
		return (num + num1)
	elif name == "/":
		return( num // num1)
	elif name == "*":
		return( num * num1)
	elif name == "-":
		return( num - num1)
	
for i in range(len(tokens),0,-1):
	if tokens[i-1].isdigit():
		if not stack2:
			stack2.append(int(tokens[i-1]))
			print(stack2)
		elif tokens[i].isdigit():
			print(tokens,tokens[i])
			stack2.append(int(tokens[i-1]))

			stack2.append(result1(stack.pop(),stack2.pop(),stack2.pop()))
			print(stack2)
		else:
			stack2.append(int(tokens[i-1]))
			
	else:
		stack.append(tokens[i-1])
while stack:
	stack2.append(result1(stack.pop(),(stack2.pop()),(stack2.pop())))

print( stack2[0])