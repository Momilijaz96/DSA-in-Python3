# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        offset=0
        queue=[(root,offset)]
        vals=[]
        level=0
        while(len(queue)>0):
            num=len(queue)
            for _ in range(num):
                node,offset = queue.pop(0)
                vals.append([node.val,offset,level])
                if node.right:
                    queue.append((node.right,offset+1))
                if node.left:
                    queue.append((node.left,offset-1))
            level+=1
        #sort by offset
        vals.sort(key=lambda x: x[1])
        
        #sort overlapping nodes with same offset and level
        temp_vals={}
        print(vals)
        pop_vals=[]
        for i in range(len(vals)-1):
            if vals[i][2]==vals[i+1][2] and vals[i][1]==vals[i+1][1]:
                key=(vals[i][1],vals[i][2])
                if key in temp_vals:
                    t=[vals[i+1][0]]
                    temp_vals[key]+=t
                else:
                    temp_vals[key]=[vals[i][0],vals[i+1][0]]
                    
                pop_vals.append(vals[i]) #append ith index
                #print(temp_vals)
                if isinstance(temp_vals[key],list):
                    temp_vals[key].sort() #sort overlapping nodes 
                vals[i+1][0]=temp_vals[key] #replace i+1th node with sorted overlapping nodes

        [vals.remove(val) for val in pop_vals] #Remove one of overlaping node
        pop_vals=[]
        #Merge nodes in same column by offset
        for i in range(len(vals)-1):
            if vals[i][1]==vals[i+1][1]:
                if isinstance(vals[i+1][0],list) and (not isinstance(vals[i][0],list)):
                    temp=[vals[i][0]]
                    temp+=vals[i+1][0] #order of the vals is important so non list first, then list item
                    vals[i+1][0]=temp
                elif isinstance(vals[i][0],list) and (not isinstance(vals[i+1][0],list)):
                    temp= vals[i][0]
                    temp+=[vals[i+1][0]]
                    vals[i+1][0]=temp
                elif (not isinstance(vals[i][0],list)) and (not isinstance(vals[i+1][0],list)):
                    vals[i+1][0]=[vals[i][0],vals[i+1][0]]
                else:
                    vals[i+1][0]=vals[i][0]+vals[i+1][0]
                    
                pop_vals.append(vals[i])
        [vals.remove(val) for val in pop_vals] #Remove multiple lists for nnodes in one col
        new_vals=[]
        for val in vals:
            if isinstance(val[0],list):
                new_vals.append(val[0])
            else:
                new_vals.append([val[0]])
        
        return new_vals
        