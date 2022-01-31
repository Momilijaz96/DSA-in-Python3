# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def list2num(self,l):
        num=0
        node=l
        place=0
        while(node):
            num+=(10**place)*int(node.val)
            place+=1
            node=node.next
        return num
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None or l2==None: return None
        num1=self.list2num(l1)
        num2=self.list2num(l2)
        res=str(num1+num2)
        
        root=ListNode(res[-1])
        node=root
        res=res[:-1]
        while(len(res)>0):
            node.next=ListNode(res[-1])
            node=node.next
            res=res[:-1]
        return root
            