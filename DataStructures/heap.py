class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def heapify(self,root_idx=0):
        if root_idx > len(self.heap): return
        left_child = (2*root_idx) + 1
        right_child = (2*root_idx) + 2
        if left_child < len(self.heap):
            if self.heap[root_idx] < self.heap[left_child]:
                self.heap[left_child],self.heap[root_idx] = self.heap[root_idx],self.heap[left_child]
            self.heapify(left_child)
        if right_child < len(self.heap):
            if self.heap[root_idx] < self.heap[right_child]:
                self.heap[right_child],self.heap[root_idx] = self.heap[root_idx],self.heap[right_child]
            self.heapify(right_child)

    def insertKey(self,x):
        self.heap.append(x)
        self.heapify()
    
    def getMax(self):
        return self.heap[0]
    
    def extractMax(self):
        self.heap.pop(0)
        self.heapify()

    def deleteKey(self,key):
        for idx,k in enumerate(self.heap):
            if k==key:
                break
        self.heap[idx] = self.getMax() + 1
        self.heapify()
        self.extractMax()
    
    def updateKey(self,old_key,new_key):
        for idx,k in enumerate(self.heap):
            if k==old_key:
                break
        self.heap[idx] = new_key
        self.heapify()

h = MaxHeap()
h.insertKey(1)
h.insertKey(2)
h.insertKey(3)
h.insertKey(5)
h.insertKey(4)
print(h.getMax()) #Max is 5

h.extractMax() #remove prev max 5
print(h.getMax()) #Max is now 4

h.deleteKey(4) #delete 4
print(h.getMax()) #max is now 3

h.updateKey(3,100) #change 3 to 100
print(h.getMax()) #new max is 100


