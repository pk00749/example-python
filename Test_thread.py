import threading
from time import sleep


def test(n, event):
    while not event.isSet():
        print('Thread %s is ready' % n)
        sleep(1)
    event.wait()
    while event.isSet():
        print(threading.current_thread().ident)
        print('Thread %s is running' % n)
        sleep(1)


def main():
    event = threading.Event()
    for i in range(2):
        th = threading.Thread(target=test, args=(i, event))
        th.start()
    sleep(1)
    print('----- event is set -----')
    event.set()
    sleep(3)
    print('----- event is clear -----')
    event.clear()


if __name__ == '__main__':
    main()