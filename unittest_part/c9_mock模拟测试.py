from unittest import mock


attrs = ['connect', 'disconnect']
# spec 参数可以给mock实例添加属性/方法, 方法调用要加()
testmock = mock.Mock(name='TestMock', spec=attrs)
print(testmock)
print(dir(testmock))
print(testmock.connect)

# return_value 给方法添加返回值
testmock.connect.return_value = 200
print(testmock.connect())

# side_effect, Mock对象返回指定的值(同一个模拟的方法,如果用了side_effect会覆盖掉return_value)
testmock.disconnect.side_effect = [100, 101, 102]
for i in range(3):
    print(testmock.disconnect())

print('-'*50)
# side_effect 也可以指向一个函数
rcode = {'ok':200, 'error':400}
def getcode(status):
    print(status)
    return rcode[status]

testmock.disconnect.side_effect = getcode

for i in rcode.keys():
    print(testmock.disconnect(i))
