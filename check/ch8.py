import base

EXPECTED = [
  "mpsc_sem passed!",
  "race adder blocking mutex passed!",
  "race adder spinning mutex passed!",
  "sync_sem passed!",
  "test_condvar passed!",
  "threads test passed!",
  "threads with arg test passed!",
  "deadlock test mutex 1 OK!",
  "deadlock test semaphore 1 OK!",
  "deadlock test semaphore 2 OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
