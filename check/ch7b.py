import base
from ch6b import EXPECTED_UNTIL_6b
from ch6 import NOT_EXPECTED

EXPECTED_7b = [
    # ch7b_pipetest.c
    "Read OK, child process exited!",
    "pipetest passed!",
]

EXPECTED_UNTIL_7b = EXPECTED_UNTIL_6b + EXPECTED_7b

TEMP = [
    # ch7b_usertest.c
    "ch7b Usertests passed!",
]


if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_7b + TEMP, NOT_EXPECTED)
