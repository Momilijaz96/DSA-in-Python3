import numpy as np
class ArrayList:
    def __init__(self):
        self.arr=np.empty(shape=(1,1))
        self.filled=0

    def add(self,val):
        if self.filled<self.arr.shape[0]:
            self.arr[self.filled]=val
            self.filled+=1
        else:
            new_arr=np.empty(shape=(self.filled*2,1)) #Resizing by 2 if capacity if full
            for i in range(self.arr.shape[0]):
                new_arr[i,0]=self.arr[i,0]
            new_arr[self.filled]=val
            self.filled+=1
            self.arr=new_arr
    
    def printAll(self):
        for i in range(self.arr.shape[0]):
            print(self.arr[i,0])


if __name__=='__main__':
    mylist = ArrayList()
    mylist.add(1)
    mylist.add(1)
    mylist.add(1)
    mylist.add(1)
    print("Array capacity: ",mylist.arr.shape)
    mylist.add(1)
    mylist.add(1)
    mylist.add(1)
    mylist.add(1)
    print("Array capacity: ",mylist.arr.shape)
    mylist.add(1)
    print("Array capacity: ",mylist.arr.shape)

    mylist.printAll()
