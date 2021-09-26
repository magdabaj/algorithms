# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
            """
        sorted_array = [0]
        # print('head', head)
        first = head
        second = head.next
        length = 1
        print(first)
        sorted_array[0] = first.val
        print(second.val)
        print('array', sorted_array)
        while second != None:
            first = second
            second = second.next
            sorted_array.append(first.val)
            print(sorted_array)

        for j in range(1, len(sorted_array)):
            print('first val', first.val)
            key = sorted_array[j]
            i = j - 1
            while i >= 0 and sorted_array[i] > key:
                print('sortedArray', sorted_array)
                sorted_array[i + 1] = sorted_array[i]
                sorted_array[i] = first.val
                i = i - 1
            print('sortedArray[i+1]', sorted_array[i + 1])
            sorted_array[i + 1] = key

        print(sorted_array)
        print(head)
        # return sortedArray

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionLinkedList:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        print("dummy", dummy)

        while curr:
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                print("prev", prev.next)
                prev = prev.next

            next = curr.next
            print('next', next)

            curr.next = prev.next
            print('prev.next', prev.next)
            prev.next = curr
            print("curr", curr)

            curr = next

        return dummy.next