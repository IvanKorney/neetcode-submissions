class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node
    

class LinkedList:
    
    def __init__(self):
        self.head  = None
        self.numNodes = 0
    
    def get(self, index: int) -> int:
        if index >= self.numNodes:
            return -1
        cur = self.head
        while index:
            index -= 1
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node
        self.numNodes += 1
        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
            return
        node = Node(val,None)
        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = node
        self.numNodes += 1

    def remove(self, index: int) -> bool:
        if index >= self.numNodes:
            return False
        
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
                    
            if cur.next == None:
                cur.next = None
            else:
                cur.next = cur.next.next


        self.numNodes -= 1
        return True

    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
        
