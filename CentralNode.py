# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def solve(self, root):
        if root==None:
            return None
        length=0
        node=root
        while(node):
            length+=1
            node=node.next
        
        k=math.ceil(length/2)
        if length%2==0: k+=1
        print(k)
        node=root
        idx=0
        while(idx<=k):
            idx+=1
            if idx==k:
                return node.val
            node=node.next
        