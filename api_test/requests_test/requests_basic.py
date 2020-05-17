import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json
base_url='http://httpbin.org'
# r1=requests.get(base_url+'/get')
# print(r1.status_code)

# r2=requests.post(base_url+'/post')
# print(r2.status_code)

# r3=requests.delete(base_url+'/delete')
# print(r3.status_code)

# r4=requests.put(base_url+'/put')
# print(r4.status_code)

#参数传递
# param={'user':'51zxw','passwd':'123456'}
# r1=requests.get(base_url+'/get',param)
# print(r1.url)
# print(r1.status_code)

# from_data={'user':'wangqian','passwd':'222222'}
# r2=requests.post(base_url+"/post",from_data)
# print(r2.text)

#请求头设置
# from_data={'user':'wangqian','passwd':'222222'}
# header={'user-agent':'Mozilla/5.0'}
# r2=requests.post(base_url+"/post",from_data,header)
# print(r2.json())
#爬去知乎
# header={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
# r=requests.get('https://www.zhihu.com/',header)
# print(r.text)

#cookie设置,超时设置
# cookie={'user':"51zxw"}
# r=requests.get(base_url+'/cookies',cookies=cookie,timeout=3)
# print(r.text)

#获取cookie,请求百度首页获取cookie
# r=requests.get('https://www.baidu.com')
# print(r.cookies)
# print(type(r.cookies))
# for key,value in r.cookies.items():
#     print(key+':'+value)

#上传文件
# file={'file':open('data.csv','rb')}
# # r=requests.post(base_url+'/post',files=file)
# # print(r.text)

#会话对象（session）
# s=requests.Session()
# r=s.get(base_url+'/cookies/set/user/51zxw')
# print(r.text)
# r=s.get(base_url+'/cookies')
# print(r.text)

#证书验证
# r=requests.get('https://www.12306.cn/index',verify=False)
# print(r.text)

#代理设置
# proxies={'https':'http://119.254.94.114:45691'}
# r=requests.get(base_url+'/get',proxies=proxies)
# print(r.text)

#身份认证
# r=requests.get(base_url+"/basic-auth/51zxw/8888",auth=HTTPBasicAuth('51zxw','8888'))
# print(r.text)
# r1=requests.get(base_url+"/digest-auth/auth/zxw/6666",auth=HTTPDigestAuth('zxw','6666'))
# print(r1.text)

#流式请求
r=requests.get(base_url+"/stream/10",stream=True)
if r.encoding is None:
    r.encoding='utf-8'
#对响应结果进行迭代处理
for line in r.iter_lines(decode_unicode=True):
    if line:
        data=json.loads(line)
        print(data['id'])
