import requests
from urllib import parse

#构造接口测试数据
data={"city":"北京"}
city=parse.urlencode(data).encode('utf-8')#将data数据中文进行编码
url='http://www.sojson.com/open/api/weather/json.shtml'

#发送请求
r=requests.get(url,params=city)
print(r.text)

#将结果转化为json类型
response_data=r.json()
#获取日期，响应信息，状态和城市
# print(response_data["date"])
print(response_data["message"])
print(response_data["status"])
print(response_data["city"])

#获取当日天气
print(response_data["data"]["forecast"][0]["date"])

