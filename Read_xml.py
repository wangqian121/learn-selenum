# 读取xml子节点
from xml.dom import minidom
dom=minidom.parse('class_info.xml')#加载xml文件
root=dom.documentElement  #获取元素信息

tags=root.getElementsByTagName('student')#获取子节点student

print(tags[0].nodeName)
print(tags[0].nodeValue)
print(tags[0].nodeType)


