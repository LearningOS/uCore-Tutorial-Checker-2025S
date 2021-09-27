import base
import ch2
from ch3 import EXPECTED, NOT_EXPECTED


EXPECTED += [
    "Test 04_0 OK!",
    "Test 04_3 test OK!",
    "Test 04_4 ummap OK!",
    "Test 04_5 ummap2 OK!",
]

NOT_EXPECTED += [
    "Should cause error, Test 04_1 fail!",
    "Should cause error, Test 04_2 fail!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
