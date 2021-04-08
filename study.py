#there is nothing...
#but someone trys encoding...

#for循环
'''
for x in y:
    循环体
'''
#读取字符串里面每一个字符
title = "大家好，我是wazty"
for i in title:
    print(i)

#for循环获取字典每一个key
dict = {'红烧肉':"20元",'盖浇饭':'10元','鸡汤':'5元'}
for key in dict:
    print("菜品：{}".format(key))
    print("价格：{}".format(dict[key]))
    print("======================")

for i in range(5):
    print("现在是第{}次循环".format(i))

p = 0
while p < 10:
    print("现在是第{}次循环".format(p))
    p += 1
#用def建立自定义函数
'''
def函数名(参数1，参数2，参数3):
    函数体第一行
    函数体第二行
    函数体第三行
    ...
    函数体第n行
    return返回值
'''
#test