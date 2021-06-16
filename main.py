import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 0.1]


def loop(n, sec, lock):
    logging.info(f"start loop{n} at {ctime()}")
    if n == 0:
        pass
    else:
        sleep(sec)
    logging.info(f"end loop{n} at {ctime()}")
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    n_loops = len(loops)
    for i in range(n_loops):
        if i == 1:
            sleep(2)
        lock = _thread.allocate_lock()     # 声明一个锁
        lock.acquire()  # 加锁
        locks.append(lock)    # 把锁传给locks
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 起一个线程
    # for i in range(n_loops):
    #     _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in range(n_loops):
        while locks[i].locked():
            pass

    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
