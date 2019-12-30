class Count(object):
    
    version = 1
    
    def add(self, x, y):
        return x+y

    def sub(self, x, y):
        return x-y

def add(x, y, *args):
    x += y
    for val in args:
        x += val
    return x

def sub(x, y, *args):
    x -= y
    for val in args:
        x -= val
    return x


if __name__=='__main__':

    print(add(10,20))
    print(add(10,20,10))

    print(sub(10,5))
    print(sub(10,5,5))