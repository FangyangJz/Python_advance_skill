
import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    # yield之前写 __enter__ 干的事情
    yield {}  
    # yield之后写 __exit__ 干的事情
    print('file end')


with file_open('boddy.txt') as f:
    print('file processing')