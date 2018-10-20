
debug后了解到scrapy中的Request和Response和普通的不太一样, 
Scrapy文档中有介绍, 我遇到的是HtmlResponse
基类 Response -> TextResponse -> HtmlResponse 和 XmlResponse

乱码问题可以通过 chardet 检测出来str是用何种方式 编码, 然后response.body是bytes类型, 就用检测到的方式decode
从二进制数据转化为文本的形式（字符集）的过程我们就称之为一个解码过程（decode），
而从字符集转化为二进制数字的过程就是一个编码（encode）过程！
gbkContent = response.body.decode(chardet.detect(response.body)['encoding'])

response的body属性不能直接修改, 修改需要用到replace方法, 返回值为update后的内容, encoding属性(不修改为cp1252, 结果是乱码)也可以一起修改掉, 如下:
gbkContent = response.body.decode('GB2312')
response = response.replace(body=gbkContent.encode('utf-8'), encoding='utf-8')