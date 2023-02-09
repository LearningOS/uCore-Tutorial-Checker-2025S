import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch7b_pipetest.c
    "Read OK, child process exited!",
    "pipetest passed!",
]

TEMP = [
    # ch7b_usertest.c
    "ch7b Usertests passed!",

]


if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
