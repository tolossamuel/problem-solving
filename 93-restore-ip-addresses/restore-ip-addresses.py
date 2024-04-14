class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid = []
        def validIp(index,temp,last,dot):
            if dot == 3:
                x = s[len(temp)-3:]
                # print(x)
                if int(x) <= 255:
                    temp += x
                    l = temp.split(".")
                    new = []
                    for i in range(len(l)):
                        if len(l[i]) > 1 and l[i][0] == "0":
                            new = []
                            break
                        new.append((l[i]))
                    if new:
                        new = ".".join(new)
                        # print(new)
                        valid.append(new)
                return 
            if int(last) > 255:
                return
            if index >= len(s):
                return 
            # print(s[index],temp,"====")
            
            validIp(index+1,temp+s[index],last+s[index],dot)
            if temp and temp[-1] != ".":
                validIp(index,temp+".","0",dot + 1)
        validIp(0,"","0",0)
        return valid
