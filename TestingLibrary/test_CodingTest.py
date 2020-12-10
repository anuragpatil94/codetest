from CodingTest import CodingTest


class Problem:
    def __init__(self):
        pass

    def TwoSum(self, arr, num):
        return [8, 4, 2]

    def OneSum(self, num):
        return num


tests = [
    {
        "function": "TwoSum",
        "params": {
            "input": [
                {"value": [1, 2, 3], "visualize": True},
                {"value": 3, "type": "float"},
            ],
            "output": [{"value": [8, 4, 2]}],
        },
    },
    # {
    #     "function": "OneSum",
    #     "params": {
    #         "input": [{"value": 3, "type": "float"},],
    #         "output": [{"value": 3}],
    #     },
    # },
]

c = CodingTest(tests)
c.run(Problem)
