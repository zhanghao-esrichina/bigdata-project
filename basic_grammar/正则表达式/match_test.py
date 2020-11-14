import re


# match 从头开始匹配
msg = '北京捷泰云际信息技术有限公司'
pattern = re.compile('北京捷泰')
pattern2 = re.compile('有限公司')

result = pattern.match(msg)
result2 = pattern2.match(msg)
result3 = re.match('北京',msg)
print(result)
print(result2)
print(result3)
