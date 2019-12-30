import os

# os.access(path, mode)
# 查看文件是否有指定权限，有则返回True否则返回flase
# path:指定文件路径
# mode:参数有F_OK(是否存在),R_OK(可读),W_OK(可写),X_OK(可执行)
r = os.access('demo.csv', os.F_OK)
print(r)
r = os.access('demo.csv', os.R_OK)
print(r)
r = os.access('demo.csv', os.W_OK)
print(r)
r = os.access('demo.csv', os.X_OK)
print(r)

print('-'*50)
# os.chdir()
# 方法用于改变当前工作目录到指定的路径。
print(os.getcwd())
os.chdir('e:\\')
print(os.getcwd())

print('-'*50)
# 3、os.chmod()
# 方法用于更改文件或目录的权限。
#  权限指定：
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读

print(os.name)  # windows返回nt, linux返回posix
file_name = os.listdir('.')
# print(file_name)
tran_file_name = [x.encode('gb2312') for x in file_name]
# print(tran_file_name)

import chardet
print(chardet.detect(tran_file_name[0]))
print(tran_file_name[-1])
print(str(tran_file_name[-1], encoding='utf-8'))

# >>> os.name #判断现在的实用平台，windows返回‘nt’,linux返回
# 'posix'
# >>> os.getcwd() #返回当前工作的目录
# '/root'
# >>> os.listdir('.') #返回指定目录下所有的文件和目录名
# ['file.txt', 'test', 'caidan.py', 'test.txt', 'test.py', 'test1.py', 'enumerate.py', 'login.py']
# >>> os.remove('test1.py') #删除指定文件
# >>> os.listdir('.')
# ['file.txt', 'test', 'caidan.py', 'test.txt', 'test.py', 'enumerate.py', 'login.py']
# >>> os.rmdir('aaa')  #删除指定目录
# >>> os.mkdir('directory')  #创建目录，只能创建一层目录
# >>>os.path.isfile()——判断指定对象是否为文件。是返回True,否则False
# >>> os.path.isfile('test.py')  #为文件返回True
# True
# >>> os.path.isfile('directory') #此为目录则返回false
# False
# >>> os.path.isdir('directory')  #判断指定对象是否为目录。
# True
# >>> os.path.exists('/python/test.py') #判断指定的对象是否存在
# True
# >>> os.path.exists('/python/caidan')
# False
# >>> os.path.split('/python/test.py') #返回路径的目录和文件名
# ('/python', 'test.py')
# >>> os.getcwd()  #获取当前工作的目录
# '/python'
# >>> os.system('pwd')  #执行shell命令
# /python
# 0
# >>> os.system("echo 'hello world!'")
# hello world!
# 0
# >>> os.path.getsize('directory') #获得文件的大小，如果为目录返回0
# 4096
# >>> os.path.abspath('.') #获得绝对路径
# '/python'
# >>> os.path.join('/python/directory/','test.py') #链接目录和文件名
# '/python/directory/test.py'
# >>> os.path.basename('/python/directory/test.py') #返回文件名
# 'test.py'
# >>> os.path.basename('/python/directory')
# 'directory'
# >>> os.path.dirname('/root/directory/test.py') #返回文件路径
# '/root/directory'
# >>> os.path.getmtime('.') #返回在此path下最后一次修改的时间戳
# 1510553280.2887046