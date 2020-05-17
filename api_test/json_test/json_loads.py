import json
#将json字符串类型转换为字典类型
# json_str='{"id":1,"name":"小王","age":12}'
# date=json.loads(json_str)
# print(type(date))
# print(date)
# print(date['id'])
# #写入json文件
# with open('date.json','w') as f:
#     json.dump(date,f,ensure_ascii=False)
#读取json文件
with open('date.json','r') as f:
    json1=json.load(f)
    print(json1)
