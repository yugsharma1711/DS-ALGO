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
            
    
    def sum(self, value, current_sum):
        if self == None:
            if current_sum == value:
                return True
            
        sum(self, value, current_sum + self.left.value)
        sum(self.right, value, current_sum + self.right.value)        