class MyLinkedList:

    def __init__(self, val=0, next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self
        print("curr", self.val)
        dummy = MyLinkedList(val=self.val)
        i = 0
        val = 0
        while i < index:
            if curr.next is None:
                return -1
            # dummy = curr.next
            curr = curr.next
            print("curr", curr.val)
            i = i + 1
        value = curr.val
        # self = dummy
        return value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr = self
        dummy = MyLinkedList()
        dummy.val = val
        if curr.next:
            dummy.next = curr.next
        self = dummy
        print("addAtHead", self.val, self.next)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self
        dummy = MyLinkedList(val)
        currCopy = MyLinkedList(val=self.val)
        print('currCopy.val', currCopy.val)
        while curr.next:
            currCopy = curr.next
        currCopy.next = dummy
        print("dummy", dummy.val)
        self = currCopy
        print("addAtTail", self.val, self.next.val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self
        dummy = MyLinkedList(val=self.val)
        i = 0
        while curr.next and i < index:
            dummy.next = curr.next
            i = i + 1
        dummy.next = MyLinkedList(val)
        if curr.next:
            dummy.next = curr.next

        self = dummy
        print("addAtIndex", self.val, self.next.val, )

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self
        dummy = MyLinkedList(val=self.val)
        i = 0
        while curr.next and i < index:
            if curr.next == None:
                break
            dummy.next = curr.next
            i = i + 1
        if curr.next and curr.next.next:
            dummy.next = curr.next.next
        while curr.next:
            dummy.next = curr.next
        self = dummy
        print("deleteAtIndex", self.val, self.next)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)