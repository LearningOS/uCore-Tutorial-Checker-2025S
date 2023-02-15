import base
from ch2b import EXPECTED_2b
from ch3 import NOT_EXPECTED

# Note: there is no test case like ch4b_xxxx, but ch3b with sleep
#  should be removed because sys_gettimeofday need to be rewritten
EXPECTED_UNTIL_4b = EXPECTED_2b + [
    # ch3b_yield0.c
    "Test write A OK!",

    # ch3b_yield2.c
    "Test write B OK!",

    # ch3b_yield1.c
    "Test write C OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED_UNTIL_4b, NOT_EXPECTED)
