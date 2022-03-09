import base

EXPECTED = [
    """Hello world from user mode program!
Test hello_world OK!""",
    """Test power OK!""",
]

TEMP = [
]

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
