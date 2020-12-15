from CodingTest import CodingTest

"""
DONE: Add Test Cases for int
DONE: Add Test Cases for int as float
DONE: Add Test Cases for int as string
DONE: Add Test Cases for Mixed types 
DONE: Add Test Cases for linkedlist as list
DONE: Add Test Cases for binarytree as list
DONE: Add Test Cases for list
DONE: Add Test Cases for bool
DONE: Add Test Cases for bool as int
DONE: Add Test Cases for dict
DONE: Add Test Cases for tuple
DONE: Add Test Cases for tuple as list
DONE: Add Test Cases for float
DONE: Add Test Cases for float as int
DONE: Add Test Cases for float as string
DONE: Add Test Cases for set
DONE: Add Test Cases for set as list
DONE: Add Test Cases for string
DONE: Add Test Cases for string as int
DONE: Add Test Cases for string as float
TODO: Comments for each function
DONE: Add Test if the function name is not passed
"""


class Problem:
    def __init__(self):
        pass

    def testDynamicInputs(self, arr, setAsArr, tupleAsArr, integerNumber, floatNumber):
        return [arr, setAsArr, tupleAsArr, integerNumber, floatNumber]

    def testInt(self, num1, num2):
        return [num1, num2]

    def testLinkedList(self, linkedlist):
        """
        This test is to check if an array is passed as a test, the 
        library will convert to array to linkedlist and then pass it to 
        the function as a param
        """
        # arr = []
        # while linkedlist:
        #     arr.append(linkedlist.val)
        #     linkedlist = linkedlist.next
        return linkedlist

    def testList(self, l):
        return l

    def testBoolean(self, booleanTrue, IntTrue, IntFalse):
        return [booleanTrue, IntTrue, IntFalse]

    def testDict(self, d):
        return d

    def testTuple(self, tup1, tup2):
        return [tup1, tup2]

    def testFloat(self, fl1, fl2):
        return [fl1, fl2]

    def testSet(self, s1, s2):
        return [s1, s2]

    def main(self):
        return "Function name not passed. default function main is executed"

    def testVariousTypesAsString(self, decimal, number):
        return [decimal, number]

    def testLinkedListOutput(self, linkedList):
        return linkedList

    def testTreeAsDict(self, d):
        pass

    def testTreeAsMultiDimentionalList(self, l):
        pass

    def testBinaryTreeAsList(self, head):
        if not head:
            return None
        head.val *= 2
        self.testBinaryTreeAsList(head.left)
        self.testBinaryTreeAsList(head.right)
        return head


tests = [
    {
        "function": "testDynamicInputs",
        "params": {
            "input": [
                {"value": [1, 2, 3]},
                {"value": [2, 3, 4], "type": "set"},
                {"value": [4, 5, 6], "type": "tuple"},
                {"value": 3},
                {"value": 3, "type": "float"},
            ],
            "output": [{"value": [[1, 2, 3], {2, 3, 4}, (4, 5, 6), 3, 3.0]}],
        },
    },
    {
        "function": "testInt",
        "params": {
            "input": [{"value": 3, "type": "float"}, {"value": 3,}],
            "output": [{"value": [3.0, 3]}],
        },
    },
    {
        "function": "testList",
        "params": {
            "input": [{"value": [1, 2, 3], "type": "list"},],
            "output": [{"value": [1, 2, 3]}],
        },
    },
    {
        "function": "testSet",
        "params": {
            "input": [{"value": [1, 2, 3], "type": "set"}, {"value": {1, 2, 3}}],
            "output": [{"value": [{1, 2, 3}, {1, 2, 3}]}],
        },
    },
    {
        "function": "testDict",
        "params": {
            "input": [{"value": {"a": 1, "b": 1}}],
            "output": [{"value": {"a": 1, "b": 1}}],
        },
    },
    {
        "function": "testTuple",
        "params": {
            "input": [{"value": (1, 2, 3)}, {"value": [1, 2, 3], "type": "tuple"}],
            "output": [{"value": [(1, 2, 3), (1, 2, 3),]}],
        },
    },
    {
        "function": "testBoolean",
        "params": {
            "input": [
                {"value": True},
                {"value": 1, "type": "bool"},
                {"value": 0, "type": "bool"},
            ],
            "output": [{"value": [True, True, False]}],
        },
    },
    {
        "function": "testFloat",
        "params": {
            "input": [{"value": 3.0}, {"value": 3, "type": "float"},],
            "output": [{"value": [3.0, 3]}],
        },
    },
    {
        "function": "testVariousTypesAsString",
        "params": {
            "input": [
                {"value": "3.0", "type": "float"},
                {"value": "3", "type": "int"},
            ],
            "output": [{"value": [3.0, 3]}],
        },
    },
    {
        "params": {
            "input": [],
            "output": [
                {"value": "Function name not passed. default function main is executed"}
            ],
        }
    },
    {
        "function": "testLinkedList",
        "params": {
            "input": [{"value": [1, 2, 3], "type": "linkedlist"},],
            "output": [{"value": [1, 2, 3]}],
        },
    },
    {
        "function": "testBinaryTreeAsList",
        "params": {
            "input": [{"value": [1, 2, 3], "type": "binarytree"},],
            "output": [{"value": [2, 4, 6]},],
        },
    },
    {
        "function": "testBinaryTreeAsList",
        "params": {
            "input": [
                {
                    "value": [1, 2, 3, 4, None, 6, 7, 8, None, None, None, 9, 10,],
                    "type": "binarytree",
                },
            ],
            "output": [
                {"value": [2, 4, 6, 8, None, 12, 14, 16, None, None, None, 18, 20]},
            ],
        },
    },
]
c = CodingTest(tests)
c.run(Problem)
