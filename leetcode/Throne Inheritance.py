class TreeNode():
    def __init__(self, name):
        self.name = name
        self.children = []
        self.dead = False
        
class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.kingName = kingName
        self.familyTree = {kingName: TreeNode(kingName)}
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        if childName not in self.familyTree:
            self.familyTree[childName] = TreeNode(childName)
        self.familyTree[parentName].children.append(self.familyTree[childName])

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.familyTree[name].dead = True

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        order = []
        stack = [self.familyTree[self.kingName]]
        while stack:
            cur_node = stack.pop()
            if not cur_node.dead:
                order.append(cur_node.name)
            for child_node in cur_node.children[::-1]:
                stack.append(child_node)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()