class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.size = 0
        # print("init", self.arr)
        return

    def get(self, i: int) -> int:
        # print("get", self.arr[i])
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        # print("set", i, n, self.arr)
        return

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1
        # print("push", self.arr)
        return

    def popback(self) -> int:
        retval = self.arr[self.size-1]
        self.size -= 1
        # print("pop", self.arr, retval)
        return retval

    def resize(self) -> None:
        self.arr += self.arr + [None] * self.capacity
        self.capacity *= 2
        # print("resize", self.arr)
        return


    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
