from multiprocessing import Process, active_children, cpu_count, Pool


def task(num):
    return 'run ---', str(num)


if __name__ == '__main__':
    print('How many CPU: {0}'.format(cpu_count()))
    print(active_children())
    with Pool(5) as p:
        print(p.map(task, [1, 2, 3]))

