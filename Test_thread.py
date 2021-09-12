# import threading
# from time import sleep
#
#
# def test(n, event):
#     while not event.isSet():
#         print('Thread %s is ready' % n)
#         sleep(1)
#     event.wait()
#     while event.isSet():
#         print(threading.current_thread().ident)
#         print('Thread %s is running' % n)
#         sleep(1)
#
#
# def main():
#     event = threading.Event()
#     for i in range(2):
#         th = threading.Thread(target=test, args=(i, event))
#         th.start()
#     sleep(1)
#     print('----- event is set -----')
#     event.set()
#     sleep(3)
#     print('----- event is clear -----')
#     event.clear()
#
#
# if __name__ == '__main__':
#     main()

import threading
from time import ctime, sleep


def func(lock):
    global gl_num
    print('Added %d, %s' % (gl_num, ctime()))
    lock.acquire()
    gl_num += 1
    sleep(1)
    print('%d, %s' % (gl_num, ctime()))
    lock.release()


if __name__ == '__main__':
    gl_num = 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=func, args=(lock,))
        t.start()
