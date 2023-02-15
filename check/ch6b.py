import base
from ch5b import EXPECTED_UNTIL_5b
from ch5 import NOT_EXPECTED

EXPECTED_6b = [
    # ch6b_filetest.c
    "filetest passed.",
    # ch6b_exec.c
    r"""argv\[0\] = \(\*o\*\)
argv\[1\] = \(>\.<\)
argv\[2\] = \(O\.O\)
argv\[3\] = \(QwQ\)
argv\[4\] = orz
argv\[5\] = 没有了呀""",
]

EXPECTED_UNTIL_6b = EXPECTED_UNTIL_5b + EXPECTED_6b

TEMP = [
    # ch6b_usertest.c
    "ch6b Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_6b + TEMP, NOT_EXPECTED)
