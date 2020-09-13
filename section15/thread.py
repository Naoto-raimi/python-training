import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1():
    # print(threading.currentThread().getName(), 'start')
    # print(threading.currentThread().getName(), 'end')
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2():
    # print(threading.currentThread().getName(), 'start')
    # print(threading.currentThread().getName(), 'end')
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')


if __name__ == '__main__':
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start()
    print(threading.enumerate())
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            continue
        thread.join()

    # t1 = threading.Thread(target=worker1)
    # # デーモン化
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # print('started')
    # # 強制終了しなくなる
    # t1.join()
    # t2.join()

    # timer
    # t = threading.Timer(3, worker1)
    # t.start()
