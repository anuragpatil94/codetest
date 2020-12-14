"""
TODO: Tree Type Class
"""


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def LinkedList(arg):
    def ListToLinkedList(arr):
        head = curr = ListNode()
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    def LinkedListToArray(l: ListNode) -> list:
        arr = []
        while l:
            arr.append(l.val)
            l = l.next
        return arr

    if arg:
        if isinstance(arg, list):
            return ListToLinkedList(arg)
        elif isinstance(arg, ListNode):
            return LinkedListToArray(arg)


class BinaryTreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def BinaryTree(arg):
    def ListToBinaryTree(arr: list):
        cur = head = BinaryTreeNode()
        cur.val = arr[0]
        q = [cur]
        for i in range(len(arr) // 2):
            cur = q.pop(0)
            if not cur:
                continue
            left = (2 * i) + 1
            right = (2 * i) + 2

            if left < len(arr) and arr[left] is not None:
                cur.left = BinaryTreeNode(arr[left])
            if right < len(arr) and arr[right] is not None:
                cur.right = BinaryTreeNode(arr[right])
            q.append(cur.left)
            q.append(cur.right)
        return head

    def BinaryTreeToList(head: BinaryTreeNode):
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

    if arg:
        if isinstance(arg, list):
            return ListToBinaryTree(arg)
        elif isinstance(arg, BinaryTreeNode):
            return BinaryTreeToList(arg)


class IOObject:
    def __init__(self, value, type=None, default=None, options={}):
        self.value = value
        self.type = type
        self.default = default
        self.options = options

    def __repr__(self):
        return str(
            {
                "value": self.value,
                "type": self.type,
                "default": self.default,
                "options": self.options,
            }
        )


class CodingTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests

    def _containerize(self, ios: list) -> list:
        knownTypes = {
            "int": int,
            "float": float,
            "complex": complex,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "str": str,
        }

        customTypes = {"linkedlist": LinkedList, "binarytree": BinaryTree}

        # TODO: Convert To Class
        def _findType(var):
            if isinstance(var, int):
                return "int"
            elif isinstance(var, float):
                return "float"
            elif isinstance(var, complex):
                return "complex"
            elif isinstance(var, list):
                return "list"
            elif isinstance(var, tuple):
                return "tuple"
            elif isinstance(var, dict):
                return "dict"
            elif isinstance(var, set):
                return "set"
            elif isinstance(var, bool):
                return "bool"

        arr = []
        for io in ios:
            value = io.pop("value")

            # Get Type from Value
            type = _findType(value)

            # if `type` is initialized then check `type` key-value in the test
            # and convert the value to that type
            if "type" in io and io["type"] != type:
                convertTo = knownTypes.get(io["type"], None) or customTypes.get(
                    io["type"], None
                )
                if convertTo is not None:
                    value = convertTo(value)
            default = io.pop("default") if "default" in io else None
            options = io
            obj = IOObject(value, type, default, options)

            arr.append(obj)
        return arr

    def toString(self):
        pass

    def visualize(self):
        pass

    def run(self, Problem):

        # For each test get input and outputs
        for test in self.tests:
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params
            params = test["params"]
            input = self._containerize(params["input"])
            output = self._containerize(params["output"])

            # Run Test on the function
            s = SingleTest(input, output)
            s.run(Problem, function)


class SingleTest:
    def __init__(self, input: [IOObject], output: [IOObject]):
        self.input = input
        self.output = output

    def run(self, cls, fn):
        knownTypes = {
            "int": int,
            "float": float,
            "complex": complex,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "str": str,
        }

        customTypes = {"linkedlist": LinkedList, "binarytree": BinaryTree}

        def _findType(var):
            if isinstance(var, int):
                return "int"
            elif isinstance(var, float):
                return "float"
            elif isinstance(var, complex):
                return "complex"
            elif isinstance(var, list):
                return "list"
            elif isinstance(var, tuple):
                return "tuple"
            elif isinstance(var, dict):
                return "dict"
            elif isinstance(var, set):
                return "set"
            elif isinstance(var, bool):
                return "bool"
            elif isinstance(var, ListNode):
                return "linkedlist"
            elif isinstance(var, BinaryTreeNode):
                return "binarytree"

        print("running test {}".format(fn))
        # get input list
        inputToTest = []
        for input in self.input:
            inputToTest.append(input.value)

        # get output
        outputOfTest = self.output[0]

        # run test
        try:
            c = cls()
            test = getattr(c, fn)
        except:
            print("Cannot find method ", fn)

        result = test(*inputToTest)
        resultType = _findType(result)

        if outputOfTest.type != resultType:
            if resultType in customTypes:
                convertTo = customTypes[resultType]
            else:
                convertTo = knownTypes.get(outputOfTest.type, None) or customTypes.get(
                    outputOfTest.type, None
                )
            if convertTo is not None:
                result = convertTo(result)
        assert result == outputOfTest.value
