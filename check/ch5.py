import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
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

    # ch5_spawn0.c
    # "Test many spawn OK!",

    # ch5_spawn1.c
    # "Test wait OK!",
    # "Test ppid OK!",
    # "Test waitpid OK!",
]
EXPECTED = list(set(EXPECTED) - set([
    "Test task info OK!",
]))

TEMP = [
    # ch5b_usertest.c
    "ch5b Usertests passed!",

    # ch5_usertest.c
    # "ch5 Usertests passed!",

    # ch5_setprio.c
    # "Test set_priority OK!",
]

NOT_EXPECTED += [
    # ch5b_exit.c
    r"wait (\d+) fail",
    "wait should fail",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
