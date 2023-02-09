import base

EXPECTED = [
    # ch2b_hello_world.c
    """Hello world from user mode program!
Test hello_world OK!""",

    # ch2b_power.c
    """Test power OK!""",
]

TEMP = [
]

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
