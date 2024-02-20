class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i]!= "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack.append(tokens[i])
            else:
                # print(stack,tokens)
                x = stack.pop()
                y = stack.pop()
                z = "1"
                if tokens[i] == "/":
                    tokens[i] = "//"
                    if x[0] == "-" and y[0] != "-":
                        x = x[1:]
                        z = "-1"
                    if y[0] == "-" and x[0] != "-":
                        y = y[1:]
                        z = "-1"
                ans = str(eval( "(" + y + tokens[i] + x + ")" +"*" + z ))
                
                stack.append(ans)
        # print(stack)
        return int(stack[0])