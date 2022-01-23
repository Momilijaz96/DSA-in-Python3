# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev=None
        curr=head
        while(curr):
            curr_next=curr.next
            curr.next=prev
            prev=curr
            curr=curr_next
        rev_head=prev
        rev_tail=head
        
        return rev_head,rev_tail
    

    def solve(self, root, k):
        if root==None: return root
        if k==1 or k==0: return root

        count=1
        pre=LLNode(-1)
        head=root
        node=root
        new_root=pre
        while(node):
            if count==k:
                post=node.next
                node.next=None
                rev_h,rev_t=self.reverse(head)
                pre.next=rev_h
                rev_t.next=post
                pre=rev_t
                node=post
                head=node
                count=1
            else:
                count+=1
                prev=node
                node=node.next
        
        if count<=k and count>1:
            node=prev
            node.next=None
            rev_h,rev_t=self.reverse(head)
            pre.next=rev_h
            rev_t.next=None

        if new_root.next:
            return new_root.next
        else:
            rev_h,rv_t= self.reverse(root)
            return rev_h


