# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root==None: return ''
        q=[root]
        node=root
        ser_tree=[root.val] #a zero in the start to make indexes start from 1
        while(len(q)>0):
            num=len(q)
            for _ in range(num):
                node=q.pop(0)
                if node.left: 
                    q.append(node.left)
                    ser_tree.append(node.left.val)
                else:
                    ser_tree.append(-1001)

                if node.right: 
                    q.append(node.right)
                    ser_tree.append(node.right.val)
                else:
                    ser_tree.append(-1001)
                
        ser_tree='_'.join(list(map(str,ser_tree)))
        print("Serialized Tree: ",ser_tree)
        return ser_tree
        
        
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data=='': return None
        data=list(map(int,data.split('_')))
        
        #Convert list to nodes
        data=list(map(lambda x: TreeNode(x) if x!=-1001 else None ,data))
        #print(data)
        root=data[0]
        lvl=1
        curr_lvl=[root]
        next_lvl=data[1:3]
        end_idx=3
        
        idx=0
        while(len(next_lvl)>0):
            #print("Current level: ",[curr_lvl])
            #print("Next level: ",[next_lvl])
            idx=0
            for node in curr_lvl:
                if node:
                    node.left=next_lvl[idx]
                    node.right=next_lvl[idx+1]
                    idx+=2
            curr_lvl=next_lvl
            non_null_curr=len(list(filter(None, curr_lvl)))
            #print("index range for next level: ",end_idx,end_idx+(non_null_curr*2))
            next_lvl=data[end_idx:end_idx+(non_null_curr*2)]
            end_idx=end_idx+(non_null_curr*2)
        
        
        
        #print("Deserialized Tree: ",data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
