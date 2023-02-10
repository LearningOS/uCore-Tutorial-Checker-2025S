import base
from ch2 import EXPECTED, NOT_EXPECTED


EXPECTED += [
    # ch3b_yield0.c
    "Test write A OK!",

    # ch3b_yield2.c
    "Test write B OK!",

    # ch3b_yield1.c
    "Test write C OK!",

    # "Test 04_0 OK!",
    # "Test 04_3 test OK!",
    # "Test 04_4 ummap OK!",
    # "Test 04_5 ummap2 OK!",
]

NOT_EXPECTED += [
    # "Should cause error, Test 04_1 fail!",
    # "Should cause error, Test 04_2 fail!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
