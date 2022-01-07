
def maxdown(node):
    if node != None:
        if node.left:
            if node.data > node.left.data:
                node.left.data = node.data
        if node.right:
            if node.data > node.right.data:
                node.right.data = node.data
        maxdown(node.left)
        maxdown(node.right)


def childsum(node):
    if node != None:
        #print("Root: ",node.data)
        if node.left == None and node.right == None:
            return
        changeTree(node.right)
        changeTree(node.left)

        if node.left:
            left = node.left.data
        else:
            left = 0

        if node.right:
            right = node.right.data
        else:
            right = 0
        if node.data < (left+right):
            node.data = left+right
        

def changeTree(node):
    maxdown(node)
    childsum(node)
