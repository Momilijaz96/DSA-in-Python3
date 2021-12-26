# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals=[]
        self.queue=[]
        self.stack=[]
    
    def level_zigzag(self,level):
        #pop and print from q
        #pop from stack and 
        #push RL onto q - for odd levels
        #push LR onto q - for even levels
        #append temp with stack
        num_nodes=len(self.stack)
        temp=[]
        for _ in range(num_nodes):
            node=self.stack.pop()
            print_node=self.queue.pop(0)
            temp.append(print_node.val)
            if (level+1)%2==0: 
                if node.right: 
                    self.queue.append(node.right)
                if node.left:
                    self.queue.append(node.left)
            else:
                if node.left:
                    self.queue.append(node.left)
                if node.right: 
                    self.queue.append(node.right)
        self.vals.append(temp)
        self.stack+=self.queue
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None: return None
        level=1
        self.queue=[root]
        self.stack=[root]
        while(len(self.queue)>0):
            self.level_zigzag(level)
            level+=1
        return self.vals
                
                    
                