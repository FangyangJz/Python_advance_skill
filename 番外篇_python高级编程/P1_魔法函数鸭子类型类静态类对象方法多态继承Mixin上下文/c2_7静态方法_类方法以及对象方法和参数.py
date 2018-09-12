class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1   # self 改实例的属性
        # Date.day += 1   #  类名.类属性 改类属性

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

    @staticmethod
    def parse_from_string(date_str):  # python中的静态方法第一参数不用self/cls
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))    
        # 静态方法这里不好, 当类名字变化, 这里要同步修改. 改进办法是使用类方法
    
    @classmethod
    def from_string(cls, date_str):  # 这里cls是常规做法, 良好的习惯. 你可以用任何,包括self, 不推荐
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day)) 

    @staticmethod
    def valid_str(date_str): # 我们做字符串判断, 类似这种操作不需要返回obj或者数值结果, 一般用静态方法
        year, month, day = date_str.split("-")
        if int(year)>0 and (int(month)<=12 and int(month)>0) and int(day)>0 :
            return True
        else:
            return False



if __name__=="__main__":
    new_day = Date(2018,12,31)
    new_day.tomorrow()   # 实际是 tomorrow(new_day)
    print(new_day)

    # 2018-12-31
    date_str = "2018-12-31"
    # year, month, day = tuple(date_str.split('-'))
    # print(year, month, day)
    # new_day = Date(int(year), int(month), int(day))  # 这里有些麻烦, 把他拿到类里面的静态方法去处理
    # print(new_day)

    # a,b,c = date_str.split('-')  这也可以
    # print(a,b,c) 

    new_day_static = Date.parse_from_string(date_str)
    print(new_day_static)

    new_day_cls = Date.from_string(date_str)
    print(new_day_cls)