from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	
def add_val(dic,key,val):
    if key not in dic:
        dic[key]=[val]
    else:
        dic[key].append(val)
    return dic
def bottomView(root):
    # Write your code here.
    if root==None: return []
    if root.left==None and root.right==None: return [root.data]
    offset=0
    q=[(root,offset)]
    vals={0: [root.data]}
    res=[]
    
    while(len(q)>0):
        node,offset=q.pop(0)
        if node.left:
            q.append((node.left,offset-1))
            vals=add_val(vals,offset-1,node.left.data)
        if node.right:
            q.append((node.right,offset+1))
            vals=add_val(vals,offset+1,node.right.data)
    
    #Take the first elem from list
    for k in vals:
        vals[k]=vals[k][-1]
    
    #Sort the keys
    keys=list(vals.keys())
    keys.sort()
    
    #store res in sorted key order
    res=[]
    for k in keys:
        res.append(vals[k])
    #print("Result: ",res)
    
    return res


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1
