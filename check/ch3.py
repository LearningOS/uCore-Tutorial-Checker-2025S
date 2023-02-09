import base
from ch2 import EXPECTED, NOT_EXPECTED, TEMP

EXPECTED += [
    # ch3b_sleep.c
    r"get_time OK! (\d+)",
    "Test sleep OK!",

    # ch3b_sleep1.c
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",

    # ch3_taskinfo.c
    # "Test task info OK!",
]

EXPECTED += [
    # ch3b_yield0.c
    "Test write A OK!",

    # ch3b_yield2.c
    "Test write B OK!",

    # ch3b_yield1.c
    "Test write C OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
