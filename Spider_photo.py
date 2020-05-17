import urllib
import urllib.request
import re
# 爬取网页图片http://p.weather.com.cn/2017/06/2720826.shtml#p=1
#解析页面
def load_page(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    data=response.read()
    return data

def get_image(html):
    regx=r'http://[\S]*jpg'#正则匹配
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html))

    num=1
    for img in get_image:
        image=load_page(img)
        with open('/Users/wangqian/Desktop/photo/%s.jpg' %num,'wb') as fb:
            fb.write(image)
            print('正在打印第%s张图片'%num)
            num=num+1
    print('下载完成')
url='http://p.weather.com.cn/2017/06/2720826.shtml#p=7'
html=load_page(url)
get_image(html)

