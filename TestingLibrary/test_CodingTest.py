from CodingTest import CodingTest

"""
DONE: Add Test Cases for int
DONE: Add Test Cases for int as float
DONE: Add Test Cases for Mixed types 
TODO: Add Test Cases for linkedlist as list
TODO: Add Test Cases for tree as dict
TODO: Add Test Cases for tree as list
TODO: Add Test Cases for binarytree as list
DONE: Add Test Cases for list
DONE: Add Test Cases for bool
TODO: Add Test Cases for dict
DONE: Add Test Cases for tuple
DONE: Add Test Cases for tuple as list
DONE: Add Test Cases for float as int
DONE: Add Test Cases for float
TODO: Add Test Cases for set
TODO: Add Test Cases for set as list
TODO: Add Test Cases for string
TODO: Add Test Cases for string vs other types 
TODO: Add Test for output as LinkedList
TODO: Comments for each function
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
        arr = []
        while linkedlist:
            arr.append(linkedlist.val)
            linkedlist = linkedlist.next
        return arr

    def testList(self, l):
        return l

    def testBoolean(self, booleanTrue):
        return booleanTrue

    def testDict(self, d):
        return d

    def testTuple(self, tup1, tup2):
        return [tup1, tup2]

    def testFloat(self, fl1, fl2):
        return [fl1, fl2]

    def testSet(self, s):
        return s


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
    # {
    #     "function": "testLinkedList",
    #     "params": {
    #         "input": [{"value": [1, 2, 3], "type": "linkedlist"},],
    #         "output": [{"value": [1, 2, 3]}],
    #     },
    # },
    {
        "function": "testList",
        "params": {
            "input": [{"value": [1, 2, 3], "type": "list"},],
            "output": [{"value": [1, 2, 3]}],
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
        "params": {"input": [{"value": True},], "output": [{"value": True}],},
    },
    {
        "function": "testFloat",
        "params": {
            "input": [{"value": 3.0}, {"value": 3, "type": "float"},],
            "output": [{"value": [3.0, 3]}],
        },
    },
]
c = CodingTest(tests)
c.run(Problem)
