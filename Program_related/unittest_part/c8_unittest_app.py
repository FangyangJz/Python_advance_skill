import os
import imghdr

# ftypes = ['png', 'jpeg', 'file', 'dir']
class CountFiles(object):
    
    ftypes = ['png', 'jpeg', 'file', 'dir']

    def __init__(self, path='./'):
        self.path = path
        self.fkinds = dict([[val,0] for val in CountFiles.ftypes])
        self.scandir()
    
    def scandir(self):
        result = os.walk(self.path)
        for info in result:
            # print(info)
            top, dirs, files = info

            self.fkinds['dir'] += len(dirs)
            for f in files:
                fpath = os.path.join(top, f)
                ftype = imghdr.what(fpath)
                if ftype == None:
                    ftype = 'file'
                self.fkinds[ftype] += 1
    
    def getInfoByKey(self, key):
        return self.fkinds[key]
    
    def cjpeg(self):
        return self.getInfoByKey('jpeg')
    
    def cpng(self):
        return self.getInfoByKey('png')
    
    def cfile(self):
        return self.getInfoByKey('file')

    def cdir(self):
        return self.getInfoByKey('dir')


if __name__ == '__main__':
    c = CountFiles(path=r'E:\Python_project_in_E\Python_Code_Skills\Python_advance_skill\unittest_part\testdir')
    print(c.fkinds)
    for key in c.ftypes:
        print('%s:%s'%(key, c.getInfoByKey((key))))