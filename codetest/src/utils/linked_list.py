class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, arg):
        pass

    def __new__(cls, arg):
        if isinstance(arg, ListNode):
            return cls.LinkedListToArray(cls, arg)
        if isinstance(arg, list):
            return cls.ListToLinkedList(cls, arg)

    def ListToLinkedList(self, arr) -> ListNode:
        head = curr = ListNode()
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def LinkedListToArray(self, l) -> list:
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        return arr
