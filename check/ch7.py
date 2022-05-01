import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
]

TEMP = [
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
