class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.tail:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        cur = self.head
        prev = None
        i = 0
        while cur and i != index:
            prev = cur
            cur = cur.next
            i += 1

        if not cur:
            return False

        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next

        if cur == self.tail:
            self.tail = prev

        return True

    def getValues(self) -> List[int]:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values
        
