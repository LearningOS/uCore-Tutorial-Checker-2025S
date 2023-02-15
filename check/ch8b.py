import base
from ch7 import NOT_EXPECTED
from ch7b import EXPECTED_UNTIL_7b

EXPECTED_8b = [
    # ch8b_mpsc_sem.c
    "mpsc_sem passed!",

    # ch8b_mut_race.c
    "race adder blocking mutex passed!",
    # ch8b_spin_mut_race.c
    "race adder spinning mutex passed!",

    # ch8b_sync_sem.c
    "sync_sem passed!",
    # ch8b_test_condvar.c
    "test_condvar passed!",

    # ch8b_threads.c
    "threads test passed!",
    # ch8b_threads_arg.c
    "threads with arg test passed!",

    # ch8b_mut_phi_din.c
    "philosopher dining problem with mutex passed!",
]

EXPECTED_UNTIL_8b = EXPECTED_UNTIL_7b + EXPECTED_8b

TEMP = [
    # ch8b_usertest.c
    "ch8b Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_8b + TEMP, NOT_EXPECTED)
