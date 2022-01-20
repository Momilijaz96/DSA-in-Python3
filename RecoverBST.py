# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root,vals):
        if root:
            self.inOrder(root.left,vals)
            vals.append(root.val)
            self.inOrder(root.right,vals)
            
    
    #function to return empty list, if passed BST is valid else returns corrupted node
    #In a valid BST, left_max<root and right_min>root
    def isValid(self,root,vals):      
        idx=vals.index(root.val)
        corr=[]
        left=vals[:idx]
        right=vals[idx+1:]
        if len(left)>0:
            if max(left)>root.val: corr.append(max(left))
            
        if len(right)>0:
            if min(right)<root.val: corr.append(min(right))
            
        if len(corr)==1: corr.append(root.val)
        return corr        
    
    def FindNode(self,x,node):
        if node:
            if node.val==x: return node
            left= self.FindNode(x,node.left)
            right= self.FindNode(x,node.right)
            return left if left else right
        
    def swapNodes(self,a,b,root):
        node=root
        node_a=self.FindNode(a,root)
        node_b=self.FindNode(b,root)
                
        temp=node_a.val
        node_a.val=node_b.val
        node_b.val=temp
        return root
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None: return root
        #Get inorder list of all nodes
        inorder=[]
        self.inOrder(root,inorder)
        #traverse nodes in inorder fashion
        stack=[root]
        node=root
        prev=None
        
        while(len(stack)>0):
            while(node):
                node=node.left
                if node: stack.append(node)
            node=stack.pop()
            corr=self.isValid(node,inorder)
            if len(corr)==2:
                print(corr)
                root=self.swapNodes(corr[0],corr[1],root)
                break
            if node.right:
                node=node.right
                stack.append(node)
            else:
                node=None
        return root
          
            
            
            
            
            
            
            
            
            
        
        