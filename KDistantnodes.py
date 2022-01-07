# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res=[] #result
        self.path=[] #path to target from root
        
    def kbelow(self,k,node):#Function to find k-distant nodes in children
        if k==0 and node!=None:
            self.res.append(node.val)
        elif node!=None and k>0:
            self.kbelow(k-1,node.left)
            self.kbelow(k-1,node.right)
    
    def path2target(self,node,target): #function to get path to target
        stack=[]
        while(1):
            while(node):
                stack.append(node)
                self.path.append(node)
                if node==target:
                    self.path.pop()
                    return 
                node=node.left
            node=stack.pop()
            if node.right:
                if node in self.path:
                    self.path=self.path[:self.path.index(node)+1]
                node=node.right
            else:
                if node==target:
                    self.path.pop()
                    return
                self.path.pop()
                node=None
            if len(stack)==0 and node==None: return
                
    def kabove(self,d,k,node,target): #function to find nodes in parents
        #d is distnace of node from target
        #k is input distance
        #node is atmost kth dsitant node from target
        
        if node!=None:
            if d<k:
                if node in self.path:
                    idx=(len(self.path)-d)+1
                    if idx<len(self.path):
                        if self.path[idx]==node.left: self.kabove(d+1,k,node.right,target)
                        else: self.kabove(d+1,k,node.left,target)
                    else:
                        if node.left==target: self.kabove(d+1,k,node.right,target)     
                        else: self.kabove(d+1,k,node.left,target)
                else:
                    self.kabove(d+1,k,node.left,target)
                    self.kabove(d+1,k,node.right,target)
            elif d==k:
                self.res.append(node.val)
                
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root.left==None and root.right==None: return []
        if root==None: return []
        if k==0: return [target.val]
        #Find k distant nodes in children
        if target.left!=None or target.right!=None:
            self.kbelow(k,target)
        
    
        #Find path to target node from root
        self.path2target(root,target)
        print("Path to target: ",[n.val for n in self.path])
        if self.path:
            #Get atmost kth highest element from target
            if len(self.path)>k: self.path=self.path[-1*k:]


            #find k distant nodes in parents
            while(len(self.path)>0):
                top=self.path[0]
                self.kabove(len(self.path),k,top,target)
                self.path.pop(0)

        return self.res
        