####################################################
#                       TREE
####################################################
class _BinaryTreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class _BinaryTree:
    def __init__(self, arg):
        pass

    def __new__(cls, arg):
        if isinstance(arg, list):
            return cls.ListToBinaryTree(cls, arg)
        elif isinstance(arg, _BinaryTreeNode):
            return cls.BinaryTreeToList(cls, arg)

    def ListToBinaryTree(self, arr: list):
        cur = head = _BinaryTreeNode()
        cur.val = arr[0]
        q = [cur]
        for i in range(len(arr) // 2):
            cur = q.pop(0)
            if not cur:
                continue
            left = (2 * i) + 1
            right = (2 * i) + 2

            if left < len(arr) and arr[left] is not None:
                cur.left = _BinaryTreeNode(arr[left])
            if right < len(arr) and arr[right] is not None:
                cur.right = _BinaryTreeNode(arr[right])
            q.append(cur.left)
            q.append(cur.right)
        return head

    def BinaryTreeToList(self, head: _BinaryTreeNode):
        cur = head
        q = [cur]
        arr = [cur.val]
        while q:
            cur = q.pop(0)
            if cur:
                if cur.left or cur.right:
                    arr.append(cur.left.val if cur.left else None)
                    arr.append(cur.right.val if cur.right else None)
                    q.append(cur.left)
                    q.append(cur.right)
            else:
                arr.append(None)
                arr.append(None)
        for i in range(len(arr) - 1, -1, -1):
            if arr[-1] is None:
                arr.pop()
            else:
                break
        return arr


####################################################
#                    LINKED LIST
####################################################
class _ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class _LinkedList:
    def __init__(self, arg):
        pass

    def __new__(cls, arg):
        if isinstance(arg, _ListNode):
            return cls.LinkedListToArray(cls, arg)
        if isinstance(arg, list):
            return cls.ListToLinkedList(cls, arg)

    def ListToLinkedList(self, arr) -> _ListNode:
        head = curr = _ListNode()
        for num in arr:
            curr.next = _ListNode(num)
            curr = curr.next
        return head.next

    def LinkedListToArray(self, l) -> list:
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        return arr
