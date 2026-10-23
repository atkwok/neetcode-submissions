class LinkedListNode:
        def __init__(self, item: int, next_node: LinkedListNode):
            self.item = item
            self.next_node = next_node

class LinkedList:
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        curr_node = self.head
        while index > 0:
            curr_node = curr_node.next_node
            index -= 1
        print ("get", index, self.getValues())
        return curr_node.item
        

    def insertHead(self, val: int) -> None:
        self.head = LinkedListNode(val, self.head)
        if self.size == 0:
            self.tail = self.head
        self.size += 1

        

    def insertTail(self, val: int) -> None:
        new_tail = LinkedListNode(val, None)
        if self.size == 0:
            self.head = new_tail
        else:
            self.tail.next_node = new_tail
        

        self.tail = new_tail
        self.size += 1
        print ("tail", self.size, self.getValues())
        
    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        change_tail_flag = False
        if index == 0:
            self.head = self.head.next_node
            self.size -= 1
            print("remove", self.getValues())
            return True
        elif index == self.size - 1:
            change_tail_flag = True

        curr_node = self.head
        future_node = self.head.next_node
        while index > 1:
            curr_node = curr_node.next_node
            index -= 1
        curr_node.next_node = curr_node.next_node.next_node

        if change_tail_flag:
            self.tail = curr_node

        self.size -= 1
        if self.size == 0:
            self.tail = None
            self.head = None
        print("remove", self.getValues())
        return True

        

    def getValues(self) -> List[int]:
        retval = [None] * self.size
        curr_node = self.head
        for i in range(self.size):
            retval[i] = curr_node.item
            curr_node = curr_node.next_node
        
        return retval
        
