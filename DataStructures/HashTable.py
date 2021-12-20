from LinkedList import LinkedList
from Node import Node
import numpy as np
import pandas as pd

class HashTable:

    #Constructor for hash table
    def __init__(self,size=100):
        self.values=pd.DataFrame(index=np.arange(size),columns=['key','value'])
        self.size=size

    #Function to add key/value pair to hash table
    def addkvpair(self,key,value):
        index = hash(key) % self.size
        if isinstance(self.values.iloc[index,0],LinkedList): #Collision with linked list at index
            self.values.iloc[index,0].addNode(data=(key,value))
        elif self.values.iloc[index].isnull()[0]:
            self.values.iloc[index]=(key,value) #No collision
        else:
            #Collision, with one kv pair at index
            data=tuple(self.values.iloc[index])
            head=Node(data)
            link_list=LinkedList(head)
            link_list.addNode(data=(key,value))
            self.values.iloc[index,0]=link_list

    #Function to lookup a key's value in hash table
    def map(self,key):
        index=hash(key) % self.size
        if isinstance(self.values.iloc[index,0],LinkedList):
            link_list=self.values.iloc[index,0]
            node=link_list.head
            #Head node check
            if node.data[0]==key:
                return node.data[1]

            while(node.next!=None):
                if(node.next.data[0]==key):
                    return node.data[1]
                node=node.next
            print("Key not found in the table!")
            return None
        elif not self.values.iloc[index].isnull()[0]:
            return self.values.iloc[index,1]
    
    #Function to delete a key,value pair from hash table
    def delete(self,key):
        key_deleted=False
        index=hash(key) % self.size
        if isinstance(self.values.iloc[index,0],LinkedList):
            list=self.values.iloc[index,0]
            node=list.head

            #Delete head node if request
            if node.data[0]==key:
                list.head=node.next
            else:               
                while(node.next!=None):
                    if(node.next.data[0]==key):
                        node.next=node.next.next
                        self.values.iloc[index,0]=list
                        key_deleted=True
                        break
                    node=node.next
                if not key_deleted:
                    print("Key not found in the Hash Table!")
        elif not self.values.iloc[index].isnull()[0]:
            self.values.iloc[index]=(np.nan,np.nan)
        else:
            print("Key not found in Hash Table!")

    #Function to update a key's value in hash table
    def updateValue(self,key,new_value):
        index=hash(key) % self.size
        if isinstance(self.values.iloc[index,0],LinkedList):
            list=self.values.iloc[index,0]
            node=list.head
            if node.data[0]==key: #Check if head node was requested for updation
                node.data=(key,new_value)
                self.values.iloc[index]=list
            else:
                while(node.next!=None):
                    if(node.next.data[0]==key):
                        node.next.data[1]=new_value
                        self.values.iloc[index,0]=list
                        break
                    node=node.next
        elif not self.values.iloc[index].isnull()[0]:
            self.values.iloc[index,1]=new_value
        else:
            print("Key not found in Hash Table!")

    #Function to get k,v pairs of the hash table
    def __call__(self):
        for index in range(self.size):
            if isinstance(self.values.iloc[index,0],LinkedList):
                print("Linked List at index ",index)
                self.values.iloc[index,0].listAll()
            elif not self.values.iloc[index].isnull()[0]:
                print("Tuple at index ",index)
                print(tuple(self.values.iloc[index]))

if __name__=='__main__':
    mydic=HashTable()
    mydic.addkvpair(0,'zero')
    mydic.addkvpair(1,'one')
    mydic.addkvpair(2,'two')
    mydic.addkvpair(3,'three')
    mydic.addkvpair(4,'four')
    #mydic()

    #Try adding a number to cause collision with index 0
    mydic.addkvpair(100,'Hundred')
    #mydic()

    ##Tr updating a key's value
    mydic.updateValue(0,'ZERO')
    mydic.updateValue(1,'ONE')
    #mydic()

    #Delete first node and mid node
    #mydic.delete(0)
    mydic.delete(4)
    mydic()

    #Retreive first,mid and last key values
    print("Key 0 value:",mydic.map(0))
    print("Key 2 value:",mydic.map(2))
    print("Key 4 value:",mydic.map(4))
    


