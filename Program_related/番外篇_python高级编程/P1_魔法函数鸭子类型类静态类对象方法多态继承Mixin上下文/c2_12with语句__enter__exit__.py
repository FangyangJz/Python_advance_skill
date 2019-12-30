# 上下文管理器 with 语句

def exec_try():
    try:
        print('code start')
        # raise KeyError
        
        # 假如在try里面有个open, 那么我们就得在finally里面写close
        # 假如每个块里面都写个return语句, 这玩意是栈结构, 永远都是finally里面返回的结果,
        # 假如finally里面没有return, 那么就返回最后return的结果
        # return 1

    except KeyError as e: 
        print("key error")
        return 2
    
    else:  # 如果不抛出异常就执行, 如果try中return了,就不执行
        print("other error")
        return 3 
    
    finally: # 咋地都执行
        print('finally')
        # return 4

# 上下文管理器
class Sample():
    def __enter__(self):
        print('enter')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do_something(self):
        print('do something')
    


if __name__ == "__main__":
    # result = exec_try()
    # print(result)

    # 上下文管理器协议, 和 魔法函数, protocol 这些挂钩
    # __enter__ 和 __exit__
    with Sample() as s:
        s.do_something()
