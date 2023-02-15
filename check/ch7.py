import base
from ch7b import EXPECTED_7b, NOT_EXPECTED
from ch6 import EXPECTED_UNTIL_6

# No task in ch7
EXPECTED_7 = EXPECTED_7b + [
]

EXPECTED_UNTIL_7 = EXPECTED_UNTIL_6 + EXPECTED_7

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_7, NOT_EXPECTED)
