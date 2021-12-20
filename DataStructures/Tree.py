class TreeNode:
    def __init__(self,data=None,children=[]):
        self.data=data
        self.children=children

#This wrapper class is optional though
class Tree:
    def __init__(self):
        self.root=TreeNode()