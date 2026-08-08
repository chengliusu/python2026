# 作者: 橙流苏
# 2026年07月18日10时09分09秒
# 知不足而奋进，望远山而前行


str1 = 'a'
print(type(str1))   # <class 'str'>
str2 = 'abc'  # python 中字符串可以用单引号
print(type(str2))   # <class 'str'>

str3 = "abc'defg"
print(str3)
str4 = 'abc\nbcd'
print(str4)
str5 = 'abc\'\"bcd'
print(str5)

str6 = 'abc\\\\bcd'
print(str6)

print('-' * 50)
print(ord('0'))     # 字符0的ASCII码值
print(chr(65))      # ASCII值为65的字符
