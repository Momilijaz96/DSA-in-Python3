from sys import stdin, setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)

# Binary tree node class for reference.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def relations(node, rel):
    if node != None:
        if node.left:
            rel[node.left] = node
        if node.right:
            rel[node.right] = node
        relations(node.left, rel)
        relations(node.right, rel)


def Burn(start, rel, time):
    if start != None and start.data != None:
        #print("Start: ", start.data, " Time: ", time)
        start.data = None
        adj_times=[time]
        if start.left and start.left.data!=None:
            adj_times.append(Burn(start.left, rel, time+1))
        if start.right and start.right.data!=None:
            adj_times.append(Burn(start.right, rel, time+1))
        if (start in rel) and (rel[start].data!=None):
            adj_times.append(Burn(rel[start], rel, time+1))
        #print("Start: ", start.data, " Time: ", time)
    return max(adj_times)


def findNode(node, start):
    if node != None:
        if node.data == start:
            return node
        res=findNode(node.left, start)
        if res==None: res=findNode(node.right, start)
        return res


def timeToBurnTree(node, start):
    start = findNode(node, start)
    #print("Start Node: ", start.data)
    rel = {}
    relations(node, rel)
    #print("Relations: ",[(k.data,v.data) for k,v in rel.items()])
    time = Burn(start, rel, 0)
    return time


# Fast input
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        start = int(input().strip())
        return None, start

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

    start = int(input().strip())

    return root, start

# main


root, start = takeInput()
print(timeToBurnTree(root, start))
