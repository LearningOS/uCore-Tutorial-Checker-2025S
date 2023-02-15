import base
from ch5 import EXPECTED_UNTIL_5, NOT_EXPECTED
from ch6b import EXPECTED_6b

EXPECTED_6 = EXPECTED_6b + [
    # ch6_file0.c
    "Test file0 OK!",
    # ch6_file1.c
    "Test fstat OK!",
    # ch6_file2.c
    "Test link OK!",
]

EXPECTED_UNTIL_6 = EXPECTED_UNTIL_5 + EXPECTED_6

TEMP = [
    # ch6_usertest.c
    "ch6 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_6 + TEMP, NOT_EXPECTED)
