class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        
        self.data = data
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end = ', ')
        if self.right:
            self.right.printTree()
            
    
    def height(self):
        if self == None:
            return 0
        return 1 + max(self.height(self.left), self.height(self.right))
    
    def checkBalanced(self):
        if self == None:
            return True
        value_1 = self.checkBalanced(self.left)
        if value_1:
            None
        else:
            return False
        value_2 = self.checkBalanced(self.right)
        if value_2:
            None
        else:
            return False
        if abs(self.height(self.left) - self.height(self.right)) > 1:
            return False
        return True