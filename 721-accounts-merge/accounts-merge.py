class Solution:
   
    def find(self,x):
        # print(x)
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)

        if self.sizes[xparent] >= self.sizes[yparent]:
            # print(xparent,yparent,"===")
            self.parent[yparent] = xparent
            self.sizes[xparent] += self.sizes[yparent]
        else:
            self.parent[xparent] = yparent
            self.sizes[yparent] += self.sizes[xparent]
    

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        m = len(accounts[0])
        self.parent = {}
        self.sizes = {}
        email_name = {}
        for x in range(n):
            for y in range(1,len(accounts[x])):
                self.parent[accounts[x][y]] = accounts[x][y]
                self.sizes[accounts[x][y]] = 1
                email_name[accounts[x][y]] = accounts[x][0]
        for x in range(n):
            for y in range(1,len(accounts[x])):
                self.union(accounts[x][1],accounts[x][y])
        # print(self.parent)
        for key in self.parent:
            self.find(key)
        group_email = defaultdict(list)
        for x in self.parent:
            group_email[self.parent[x]].append(x)
        # print(group_email)
        ans = []
        for x in group_email:
            email = sorted(group_email[x])
            email = [email_name[x]] + email
            ans.append(email)
        # print(ans)/
        return ans
