from timeit import default_timer as timer
from utils._type import _Type
from utils._ioobject import _IOObject


class CodeTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests

    def run(self, Problem):

        # For each test get input and outputs
        for index, test in enumerate(self.tests):
            # function to test
            function = test["function"] if "function" in test else "main"

            # get input and output params
            params = test["params"]
            inputParams = self._containerize(params["input"])
            outputParams = self._containerize(params["output"])

            # Run Test on the function
            sTest = _SingleTest(Problem, function, index, inputParams, outputParams)
            sTest.run()

    def _containerize(self, ios: list) -> list:
        """Creates a list of IOObject Object containing ios data"""
        Type = _Type()
        arr = []
        for io in ios:
            data = io.pop("value")

            conversionTypeString = io.pop("type") if "type" in io else None
            conversionTypeString, conversionTypeClass = Type.getConversionType(
                data, conversionTypeString
            )

            data = conversionTypeClass(data)
            default = io.pop("default") if "default" in io else None
            options = io
            obj = _IOObject(data, conversionTypeString, default, options)
            arr.append(obj)
        return arr

    def visualize(self):
        pass


class _SingleTest:
    def __init__(self, cls, fn, testIndex, input: [_IOObject], output: [_IOObject]):
        self.cls = cls
        self.fn = fn
        self.testIndex = testIndex
        self.input = input
        self.output = output

    def _getInputArray(self):
        pass

    def _getOutputArray(self):
        pass

    def _getErrorMessage(self, expectedOutput, actualOutput, time):
        strExpectedOut = str(expectedOutput)
        strActualOut = str(actualOutput)

        minHorizontalLen = 60

        heading = "[TEST {}]".format(str(self.testIndex)).center(minHorizontalLen, "-")
        txt = """{}\nExpected Output: {}\nActual Output:   {}\n{}\n{}
        """.format(
            heading,
            strExpectedOut,
            strActualOut,
            str(("[Time: " + str(round(time * 1000, 3))) + "ms]").rjust(
                minHorizontalLen
            ),
            "".center(minHorizontalLen, "-"),
        )
        return txt

    def run(self):
        # get input list
        inputParams = []
        for input in self.input:
            inputParams.append(input.value)

        # get output
        outputIOObject = self.output[0]

        # run test
        try:
            DynamicClass = self.cls()
            testFunction = getattr(DynamicClass, self.fn)
        except:
            print("Cannot find method ", self.fn)

        start = timer()
        output = testFunction(*inputParams)
        end = timer()
        totaltime = end - start

        Type = _Type()

        conversionTypeString, conversionTypeClass = Type.getConversionType(
            output, outputIOObject.type
        )
        output = conversionTypeClass(output)
        try:
            assert output == outputIOObject.value
        except Exception as e:
            print(self._getErrorMessage(outputIOObject.value, output, totaltime))

    def _execute(self, *args):
        pass

