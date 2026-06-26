class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        old_head = self.head
        self.head = Node(val=val, next=old_head)
        if not old_head:
            self.tail = self.head
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_tail = Node(val=val, next=None)
        if not self.tail:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return True

        prev = self.head
        curr = self.head.next
        i = 1
        while curr:
            if i == index:
                prev.next = curr.next
                if i == self.size - 1:
                    self.tail = prev
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
