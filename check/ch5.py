import base
from ch4 import EXPECTED_UNTIL_4
from ch5b import EXPECTED_5b, NOT_EXPECTED

EXPECTED_5 = EXPECTED_5b + [
    # ch5_spawn0.c
    "Test many spawn OK!",

    # ch5_spawn1.c
    "Test wait OK!",
    "Test ppid OK!",
    "Test waitpid OK!",
]

EXPECTED_UNTIL_5 = EXPECTED_UNTIL_4 + EXPECTED_5
# Task info should be removed becase assert(info.time < t3 - t1 + 100); may fail
EXPECTED_UNTIL_5.remove("Test task info OK!")

TEMP = [
    # ch5_usertest.c
    "ch5 Usertests passed!",

    # ch5_setprio.c
    "Test set_priority OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_5 + TEMP, NOT_EXPECTED)
