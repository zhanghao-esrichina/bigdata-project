import re

msg = '北京捷泰云际信息技术有限公司'
result = re.search('捷泰', msg)
print(result)
print(result.span())
print(result.start())
print(result.end())
print(result.string)
print(result.groups())  # 
print(result.group())  # 使用group提取到匹配到内容


print('================demo2==================')
username = 'admin001.'

result2 = re.match('[a-zA-Z][0-9a-zA-Z]{5,}', username)
result3 = re.search('^[a-zA-Z][0-9a-zA-Z]{5,}$',username)  # $表示整个字符串到匹配
print(result2)
print(result3) 
