from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
def add_val(dic,key,val):
    if key not in dic:
        dic[key]=[val]
    else:
        dic[key].append(val)
    return dic
def getTopView(root):
    # Write your code here.
    if root==None: return []
    if root.left==None and root.right==None: return [root.val]
    offset=0
    q=[(root,offset)]
    vals={0: [root.val]}
    res=[]
    
    while(len(q)>0):
        node,offset=q.pop(0)
        if node.left:
            q.append((node.left,offset-1))
            vals=add_val(vals,offset-1,node.left.val)
        if node.right:
            q.append((node.right,offset+1))
            vals=add_val(vals,offset+1,node.right.val)
    
    #Take the first elem from list
    for k in vals:
        vals[k]=vals[k][0]
    
    #Sort the keys
    keys=list(vals.keys())
    keys.sort()
    
    #store res in sorted key order
    res=[]
    for k in keys:
        res.append(vals[k])
    #print("Result: ",res)
    
    return res


# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)