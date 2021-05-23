from multiprocessing import Process, Queue

# 队列是线程和进程安全的
def f(q):
    q.put([42, None, 'Hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())
    p.join()
