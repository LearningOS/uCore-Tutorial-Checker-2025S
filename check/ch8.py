import base

EXPECTED = [
    """Hello world from user mode program!
Test hello_world OK!""",
    """Test power OK!""",
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
    "forktest0 pass.",
    "forktest1 pass.",
    "forktest2 test passed!",
    "Test getpid OK! pid = (\d+), ppid = (\d+)"
    "mpsc_sem passed!",
    "filetest passed.",
    "race adder blocking mutex passed!",
    "race adder spinning mutex passed!",
    "sync_sem passed!",
    "test_condvar passed!",
    "threads test passed!",
    "threads with arg test passed!",
    "philosopher dining problem with mutex passed!",
    "deadlock test mutex 1 OK!",
    "deadlock test semaphore 1 OK!",
    "deadlock test semaphore 2 OK!",
    "ch8 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED, [])
