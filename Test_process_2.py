from multiprocessing import Process
import os


def f(name):
    print('Hello', name)
    print('Parent Process ID: ', os.getppid())
    print('Process ID: ', os.getpid())


if __name__ == '__main__':
    p = Process(target=f, args=('York',))
    p.start()
    p.join()
