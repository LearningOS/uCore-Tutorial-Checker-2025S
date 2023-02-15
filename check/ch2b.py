import base

EXPECTED_2b = [
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
    base.test(EXPECTED_2b + TEMP, NOT_EXPECTED)
