# def product(*x):
#     sum=1
#     for i in x:
#         sum=sum*i
#     return sum
#
# print(product(2,3,2))
# import os
# a=os.listdir(".")
# print(a)
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s for s in L1 if isinstance(s,str)=='true']
# print(L2)
# print(isinstance(None,str))
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x for x in L1 if isinstance(x, str)]   #判斷L1為字符串的元素輸入到L2

print(L2)