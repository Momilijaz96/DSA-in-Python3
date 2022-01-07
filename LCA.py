# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findNode(self,root,mynode):
        stack=[]
        curr=[]
        node=root
        while(1):
            while(node):
                stack.append(node)
                curr.append(node)
                if node==mynode:
                    return curr
                node=node.left
            node=stack.pop()
            if node.right:
                if node in curr:
                    curr=curr[:curr.index(node)+1]
                node=node.right
            else:
                if node==mynode:
                    return curr
                curr.pop()
                node=None
            if len(stack)==0 and node==None: return []
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p==None or q==None or root==None: return None
        node=root
        #Find p
        p_stack=self.findNode(root,p)
        print([p.val for p in p_stack])
        #find q
        q_stack=self.findNode(root,q)
        print([q.val for q in q_stack])
        short_st=q_stack if len(q_stack)<len(p_stack) else p_stack
        #Return the LCA
        for i in range(len(short_st)):
            if q_stack[i]!=p_stack[i]:
                return q_stack[i-1]
        return short_st[-1]