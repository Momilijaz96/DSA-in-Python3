from DataStructures.BinaryTree import BinaryNode

#This func return height of tree if it's balanced otherwise -1
def check(node):
    if node==None: return 0
    left_depth=check(node.left)
    right_depth=check(node.right)
    diff=abs(left_depth-right_depth)
    if diff>1 or left_depth==-1 or right_depth==-1:
        return -1
    return 1+max(left_depth,right_depth)

def isBalanced(node):
    return check(node)!=-1