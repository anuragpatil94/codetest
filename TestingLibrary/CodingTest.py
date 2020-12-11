"""
TODO: Linked list Type Class
TODO: Tree Type Class
"""


class IOObject:
    def __init__(self, value, type, default, options={}):
        self.value = value
        self.type = type
        self.default = default
        self.options = options


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

            type = _findType(value)
            if "type" in io and io["type"] != type:
                convertTo = knownTypes[io["type"]]
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
        print("running test {}".format(fn))
        # get input list
        inputToTest = []
        for input in self.input:
            inputToTest.append(input.value)

        # get output
        outputOfTest = self.output[0].value

        # run test
        try:
            c = cls()
            test = getattr(c, fn)
        except:
            print("Cannot find method ", fn)

        result = test(*inputToTest)
        assert result == outputOfTest
