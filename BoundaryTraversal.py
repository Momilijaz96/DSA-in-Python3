# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftQualify(prev,node,prev_qualify):
    cnd1=(node.left==None and node.right==None) #if leaf print it
    if prev and prev_qualify:
        cnd2=(prev.left==node) #if left node on left side print it
        cnd3=(prev.left==None and prev.right==node) #if right child of a prent with no left print i
    else:
        cnd2=False
        cnd3=False
    if cnd1 or cnd2 or cnd3:
        return True
    return False

def rightQualify(prev,node,prev_qualify):
    cnd1= (node.left==None and node.right==None) #if leaf print it
    if prev and prev_qualify:
        cnd2= (prev.right==node) #if right node on left side print it
        cnd3= (prev.right==None and prev.left==node) #if left child of a prent with no right print i
    else:
        cnd2=False
        cnd3=False
    if cnd1 or cnd2 or cnd3:
        return True
    return False
    
def traverseBoundary(root):
    if root.left==None and root.right==None: return [root.data]
    if root==None: return []
    stack=[]
    prev=None
    node=root
    vals=[]
    prev_qualify=True
    if root.left:
        while(1): #Left descendant
            while(node):
                if node.right: stack.append(node.right)
                prev_qualify=leftQualify(prev,node,prev_qualify) or node==root
                if prev_qualify: 
                    vals.append(node.data)
                prev=node
                node=node.left
            node=stack.pop() if len(stack)>0 else None
            if len(stack)==0 and (node==None or node==root.right): break
    if root.right:
        stack=[] 
        right_stack=[]
        prev=root
        prev_qualify=True
        while(1): #Right descendant
            while(node):
                if node.left: stack.append(node.left)
                prev_qualify=rightQualify(prev,node,prev_qualify) or node==root
                if prev_qualify: 
                    right_stack.append(node.data)
                prev=node
                node=node.right
            node=stack.pop() if len(stack)>0 else None
            if (not node) and (len(stack)==0):
                break
        if right_stack[0]==root.data: 
            right_stack=right_stack[1:]+[root.data]

        vals+=(right_stack[::-1])
    return vals
    

            
    
