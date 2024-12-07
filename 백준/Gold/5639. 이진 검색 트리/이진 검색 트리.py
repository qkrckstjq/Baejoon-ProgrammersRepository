import sys
sys.setrecursionlimit(10001)

class BT():
    value = None
    left = None
    right = None
    
    def __init__(self, value):
        self.value = value
    
    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BT(value)
        else:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BT(value)

tree = BT(None)
while True:
    value = 0
    try:
        value = int(input())
        tree.insert(value)
    except:
        break
    
def dfs(node):
    if node == None:
        return
    dfs(node.left)
    dfs(node.right)
    print(node.value)

dfs(tree)