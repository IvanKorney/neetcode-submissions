class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None]*self.cap
        self.curIndex = 0

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.curIndex == self.cap:
            self.resize()
        self.arr[self.curIndex] = n
        self.curIndex += 1

    def popback(self) -> int:
        a = self.arr[self.curIndex-1]
        self.arr[self.curIndex-1] = None
        self.curIndex -= 1
        return a
 

    def resize(self) -> None:
        self.arr = self.arr + [None]*self.cap
        self.cap *= 2


    def getSize(self) -> int:
        return self.curIndex 
        
    
    def getCapacity(self) -> int:
        return self.cap
