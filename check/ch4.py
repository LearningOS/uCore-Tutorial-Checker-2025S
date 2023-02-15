import base
from ch4b import EXPECTED_UNTIL_4b, NOT_EXPECTED
from ch3 import EXPECTED_UNTIL_3


EXPECTED_4 = [
    # ch4_mmap0.c
    "Test 04_0 OK!",
    # ch4_mmap3.c
    "Test 04_3 test OK!",
    # ch4_unmap0.c
    "Test 04_4 ummap OK!",
    # ch4_unmap1.c
    "Test 04_5 ummap2 OK!",
]

EXPECTED_UNTIL_4 = EXPECTED_UNTIL_3 + EXPECTED_4

NOT_EXPECTED += [
    # ch4_mmap1.c
    "Should cause error, Test 04_1 fail!",
    # ch4_mmap2.c
    "Should cause error, Test 04_2 fail!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_4, NOT_EXPECTED)
