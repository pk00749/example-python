from logutils import LOGUTILS

log = LOGUTILS()
root = log.queue_handler()

def test_1():
    root.info('Hello')
