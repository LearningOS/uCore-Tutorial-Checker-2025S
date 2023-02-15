import base
from ch3b import EXPECTED_UNTIL_3b
from ch4 import NOT_EXPECTED

EXPECTED_5b = [
    # ch5b_exit.c
    "exit pass.",

    # ch5b_forktest0.c
    "forktest0 pass.",
    # ch5b_forktest1.c
    "forktest1 pass.",
    # ch5b_forktest2.c
    "forktest2 test passed!",

    # ch5b_getpid.c
    "Test getpid OK!",
]

EXPECTED_UNTIL_5b = EXPECTED_UNTIL_3b + EXPECTED_5b

TEMP = [
    # ch5b_usertest.c
    "ch5b Usertests passed!",
]

NOT_EXPECTED += [
    # ch5b_exit.c
    r"wait (\d+) fail",
    "wait should fail",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_5b + TEMP, NOT_EXPECTED)
