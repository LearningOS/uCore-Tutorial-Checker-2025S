import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test many spawn OK!",
    "Test wait OK!",
    "Test ppid OK!",
    "Test waitpid OK!",
]

DONOTTEST = [
    "Test task info OK!",
]

TEMP = [
    "ch5 Usertests passed!",
    "Test set_priority OK!",
]

if __name__ == '__main__':
    base.test(list(set(EXPECTED + TEMP) - set(DONOTTEST)), NOT_EXPECTED)
