import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch6b_filetest.c
    "filetest passed.",
    # ch6b_exec.c
    r"""argv\[0\] = \(\*o\*\)
argv\[1\] = \(>\.<\)
argv\[2\] = \(O\.O\)
argv\[3\] = \(QwQ\)
argv\[4\] = orz
argv\[5\] = 没有了呀""",

    # ch6_file0.c
    # "Test file0 OK!",
    # ch6_file1.c
    # "Test fstat OK!",
    # ch6_file2.c
    # "Test link OK!",
]

TEMP = [
    # ch6b_usertest.c
    "ch6b Usertests passed!",

    # ch6_usertest.c
    # "ch6 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
