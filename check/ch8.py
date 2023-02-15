import base
from ch8b import EXPECTED_8b, NOT_EXPECTED
from ch7 import EXPECTED_UNTIL_7

EXPECTED_8 = EXPECTED_8b + [
    # ch8_mut1_deadlock.c
    "deadlock test mutex 1 OK!",
    # ch8_sem1_deadlock.c
    "deadlock test semaphore 1 OK!",
    # ch8_sem2_deadlock.c
    "deadlock test semaphore 2 OK!",
]

EXPECTED_UNTIL_8 = EXPECTED_UNTIL_7 + EXPECTED_8

TEMP = [
    # ch8_usertest.c
    "ch8 Usertests passed!"
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_8 + TEMP, NOT_EXPECTED)
