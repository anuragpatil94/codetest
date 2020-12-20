from .ds import *

class _Type:
    def __init__(self):
        pass

    def getDefaultTypeAsClass(self, typeAsString):
        defaultTypes = {
            "int": int,
            "float": float,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "str": str,
        }
        return defaultTypes.get(typeAsString, None)

    def getCustomTypeAsClass(self, typeAsString):
        customTypes = {
            "linkedlist": LinkedList,
            "binarytree": BinaryTree,
        }
        return customTypes.get(typeAsString, None)

    def getTypeAsString(self, data) -> str:
        if isinstance(data, int):
            return "int"
        elif isinstance(data, str):
            return "str"
        elif isinstance(data, float):
            return "float"
        elif isinstance(data, list):
            return "list"
        elif isinstance(data, tuple):
            return "tuple"
        elif isinstance(data, dict):
            return "dict"
        elif isinstance(data, set):
            return "set"
        elif isinstance(data, bool):
            return "bool"
        elif isinstance(data, ListNode):
            return "linkedlist"
        elif isinstance(data, BinaryTreeNode):
            return "binarytree"

    def getConversionType(self, data, conversionTypeString=None):
        actualDataTypeString = self.getTypeAsString(data)

        if self.getCustomTypeAsClass(actualDataTypeString) or not conversionTypeString:
            return (
                actualDataTypeString,
                self.getCustomTypeAsClass(actualDataTypeString)
                or self.getDefaultTypeAsClass(actualDataTypeString),
            )

        if conversionTypeString:
            return (
                conversionTypeString,
                self.getCustomTypeAsClass(conversionTypeString)
                or self.getDefaultTypeAsClass(conversionTypeString),
            )

