import requests
import multiprocessing


def test():
    res = requests.get('http://127.0.0.1:5000/')
    print(res)


if __name__ == '__main__':
    workers = []
    for i in range(5):
        wp = multiprocessing.Process(target=test)
        workers.append(wp)
        wp.start()

    for worker in workers:
        worker.join()

