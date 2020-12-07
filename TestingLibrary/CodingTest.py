class IOObject:
    def __init__(self, value, type, default, options={}):
        self.value = value
        self.type = type
        self.default = default
        self.options = options


class CodingTest:
    def __init__(self, tests: list) -> None:
        self.tests = tests
        pass

    def getInputs(self):
        pass

    def getResults(self):
        pass

    def toString(self):
        pass

    def visualize(self):
        pass

    def run(self):
        inputs = []
        results = []
        pass


class SingleTest:
    def __init__(self, input, output):
        self
