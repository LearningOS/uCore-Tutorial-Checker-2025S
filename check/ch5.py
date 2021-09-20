import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test many spawn OK!",
    "Test wait OK!",
    "Test ppid OK!",
    "Test waitpid OK!",
]

TEMP = [
    "ch5 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
