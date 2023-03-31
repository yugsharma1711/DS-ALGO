from collections import deque
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
    
    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.data, end = ', ')
        if self.right:
            self.left.inorderTraversal()   
    
    def preorderTraversal(self):
        print(self.data, end = ', ')
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()
    
    def postorderTraversal(self):
        
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()   
        print(self.data,end = ', ')  
    
    def levelorderTraversal(self):
        queue = deque()
        queue.append(self)
        answer = [[self.data]]
        while len(queue) != 0:
            level = []
            top_element = queue[0] 
            queue.popleft()
            if top_element.left:
                queue.append(top_element.left)
                level.append(top_element.left.data)
            if top_element.right:
                queue.append(top_element.right)
                level.append(top_element.right.data)
            answer.append(level)
        print(answer)
            
            
                
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print('Inorder')
root.inorderTraversal()
print()
print('Preorder')
root.preorderTraversal()
print()
print('Postorder')
root.postorderTraversal()
print()
print('Level Order')
root.levelorderTraversal()