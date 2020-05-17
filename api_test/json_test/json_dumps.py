import json
#将字典类型转换为json字符串类型
date={"id":1,"name":"小王","age":12}
print(type(date))
json_str=json.dumps(date,ensure_ascii=False)
print(type(json_str))
print(json_str)