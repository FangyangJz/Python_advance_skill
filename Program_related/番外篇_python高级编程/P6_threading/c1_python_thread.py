# 对于IO操作, 多线程和多进程性能差别不大


import time
import threading


# 1. 通过Thread类实例化
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


# 2. 通过集成Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":

## 1. 通过Thread类实例化
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    #
    # # thread1.setDaemon(True)
    # # thread2.setDaemon(True)   # 控制线程执行, 要么用setDaemon 要么用join
    #
    # start_time = time.time()
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()  # join 会让主线程阻塞在此处, 要等子线程执行完才能继续往下执行print
    # thread2.join()
    #
    # # 当主线程退出的时候, 子线程kill掉, 用setDaemon(True), 将上面的连个线程设置成守护线程
    # # 当主线程结束后, 关闭守护线程
    # print("last time: {}".format(time.time() - start_time))

## 2. 通过集成Thread来实现多线程 (更常用, 更专业)
    thread1 = GetDetailHtml("get html")
    thread2 = GetDetailUrl("get url")
    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time : {}".format(time.time() - start_time))