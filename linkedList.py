class Node:

    # Function to initialise the node object
    def __init__(self, val=0, next=None):
        self.val = val  # Assign data
        self.next = None  # Initialize next as null


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count = count + 1

        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length():
            return -1
        curr = self.head
        i = 0
        while i < index:
            if curr.next is None or self.head is None:
                return -1
            # dummy = curr.next
            curr = curr.next
            i += 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        dummy = Node(val, next=None)
        if self.head is None:
            self.addAtHead(val)
            return
        for i in range(self.length() - 1):
            curr = curr.next
        curr.next = dummy

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head
        dummy = Node(val)
        if index < 0 or index > self.length():
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length():
            self.addAtTail(val)
            return
        for i in range(index - 1):
            curr = curr.next

        dummy.next = curr.next
        curr.next = dummy

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length():
            return
        curr = self.head
        if index == 0:
            self.head = self.head.next
            return
        for i in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)