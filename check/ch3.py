import base
from ch2b import EXPECTED_2b
from ch3b import EXPECTED_3b, NOT_EXPECTED, TEMP

EXPECTED_3 = EXPECTED_3b + [
    # ch3_taskinfo.c
    "Test task info OK!",
]

EXPECTED_UNTIL_3 = EXPECTED_2b + EXPECTED_3

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_3 + TEMP, NOT_EXPECTED)
