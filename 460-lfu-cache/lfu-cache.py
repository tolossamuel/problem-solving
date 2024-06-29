from collections import defaultdict
from collections import OrderedDict
class Node:
    def __init__(self, key, val ,count):
        self.key = key
        self.val = val
        self.count = count
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}
        self.countToNode = defaultdict(OrderedDict)
        self.mini = None
    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        del self.countToNode[node.count][key]
        if not self.countToNode[node.count]:
            del self.countToNode[node.count]
        node.count += 1
        self.countToNode[node.count][key] = node
        if not self.countToNode[self.mini]:
            self.mini += 1
        return node.val
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.get(key)
            return
        if len(self.keyToNode) == self.capacity:
            k, n = self.countToNode[self.mini].popitem(last = False)
            del self.keyToNode[k]
        self.countToNode[1][key] = self.keyToNode[key] = Node(key, value, 1)
        self.mini = 1

        return
    