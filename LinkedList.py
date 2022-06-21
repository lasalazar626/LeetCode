class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node()
    def get(self, index: int) -> int:
        if index>= self.length():
            return -1
        cur = self.head
        for i in range(0,index):
            if cur.next:
                cur=cur.next
        return cur.val if cur.val != None else -1
    def addAtHead(self, val: int) -> None:
        if self.head.val == None:
            self.head = Node(val)
        else:
            cur = self.head
            newNode = Node(val)
            newNode.next = cur
            self.head = newNode
    def length(self) -> int:
        if self.head == None:
            return 0   
        cur = self.head
        length = 1
        while cur.next!=None:
            length += 1
            cur = cur.next
        return length
        
    def addAtTail(self, val: int) -> None:
        if self.head.val == None:
            self.head = Node(val)
        else:    
            newNode = Node(val)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
        
    def display(self) -> list:
        temp = []
        cur = self.head
        while cur!= None:
            temp.append(cur.val)
            cur = cur.next
        return temp
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length()+1:
            return "Out of range"
        if index == self.length()+1:
            return self.addAtTail(val)
        cur = self.head
        newNode = Node(val)
        if index == 0:
            return self.addAtHead(val)
            
        for i in range(0,index):
            if i == index -1:
                prev = cur
            cur = cur.next
        prev.next = newNode
        newNode.next = cur
        

    def deleteAtIndex(self, index: int) -> None:
        # deleting head
        #delete inbetween nodes
        #delete final node
        cur = self.head
        if index >= self.length():
            return "Out of range"
        if index == 0:
            self.head = cur.next
        else:
            for i in range(0,index):
                if i == index-1:
                    prev = cur
                cur = cur.next
            prev.next = cur.next
