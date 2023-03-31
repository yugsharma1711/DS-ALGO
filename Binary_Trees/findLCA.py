#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        final_p = []
        final_q = []
        findChild(root, n1, n2, [False], [], [False], [], final_p, final_q)
        i = 0
        j = 0
        lowest_ancestor = 0
        while i < len(final_p) and j < len(final_q):
            if final_p[i].data == final_q[j].data:
                lowest_ancestor = final_q[i]
            i += 1
            j += 1
            
        print(lowest_ancestor.data)
        return root
answer = []
def findChild(root,p, q, p_found, p_ans, q_found, q_ans, final_p, final_q):
    if root == None:
        return
    if p_found[0] is False:
        p_ans.append(root)
        if root.data == p:
            p_found[0] = True
            final_p += p_ans
        
    if q_found[0] is False:
        q_ans.append(root)
        if root.data == q:
            q_found[0] = True
            final_q += q_ans
        
    if root.left:
        findChild(root.left, p, q, p_found, p_ans[:], q_found, q_ans[:], final_p, final_q)
    if root.right:
        findChild(root.right, p, q, p_found, p_ans[:], q_found, q_ans[:], final_p, final_q)
                


from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
        a,b=[5,1]
        s= '3 5 1 6 2 0 8 N N 7 4'
        root=buildTree(s)
        Solution().lca(root,a,b)



# } Driver Code Ends