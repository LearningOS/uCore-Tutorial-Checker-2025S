import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test many spawn OK!",
    "Test wait OK!",
    "Test ppid OK!",
    "Test waitpid OK!",
]
EXPECTED = list(set(EXPECTED) - set([
    "Test task info OK!",
]))

TEMP = [
    "ch5 Usertests passed!",
    "Test set_priority OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
