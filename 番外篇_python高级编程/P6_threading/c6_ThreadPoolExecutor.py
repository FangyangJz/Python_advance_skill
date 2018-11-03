from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED

# 线程池
# 主线程中可以获取某一个线程的状态或某一个任务的状态, 以及返回值
# 当一个线程完成时, 我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致

import time

def get_html(times):
    time.sleep(times)
    print('got page {} success'.format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# # 通过submit函数提交执行的函数到线程池
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
# # submit的返回值可以判断是否执行成功
# print(task1.done())  # done方法用于判定某个任务是否完成
# print(task2.cancel())  # 一旦线程开始执行了, 那么就不能cancel, 返回false, 执行前可以cancel成功(将max_workers=1, 返回true)
# time.sleep(4)
# print(task1.done())
# print(task1.result())  # result方法可以获取task的执行结果


# !! 以上不是太常用, 常用的是获取已经成功的task的返回, as_completed
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls] # 批量提交
# as_completed 源码里面有yield, 是个生成器
for future in as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

print('-'*50)
# 通过executor获取已经完成的task
for data in executor.map(get_html, urls):
    print("get {} page success".format(data))

wait(all_task, return_when=FIRST_COMPLETED)   # 默认值ALL_COMPLETED等所有线程执行完, 在执行接下来的主线程
print("main")