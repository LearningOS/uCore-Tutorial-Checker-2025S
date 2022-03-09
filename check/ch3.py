import base
from ch2 import EXPECTED, NOT_EXPECTED, TEMP

EXPECTED += [
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
    "Test task info OK!",
]

EXPECTED += [
    "Test write A OK!",
    "Test write B OK!",
    "Test write C OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
