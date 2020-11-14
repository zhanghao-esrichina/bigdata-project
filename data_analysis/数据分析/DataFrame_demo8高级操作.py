import numpy as np
import pandas as pd
import sqlite3


'''
替换操作

'''
print('\n=====================替换操作==========================')
df = pd.DataFrame(data=np.random.randint(0, 5, size=(5, 6)))
print(df)

print('\n替换')
print(df.replace(to_replace=2, value='two'))
print(df.replace(to_replace={1: 'one'}))
print('\n替换第四列的3替换成three')
print(df.replace(to_replace={4: 3}, value='three'))
'''
to_replace{列标签：被替换值}
'''

'''
映射操作
创建一个映射关系，把values元素和一个特定的标签或者字符串绑定（给一个元素提供不同的表现形式）

创建一个df，两列分别是姓名和薪资，然后给其名字起对应的英文名
'''
print('\n=====================映射操作==========================')
dic = {'name': ['张三', '李四', '张三'],
       'salary': [10000, 15000, 10000]}
df = pd.DataFrame(data=dic)
print(df)
print('映射关系表')
dic2 = {'张三': 'tome', '李四': 'jack'}
df['english_name'] = df['name'].map(dic2)
print(df)

'''
运算工具
需求：超过3000部分的钱缴纳50%的税收，计算每个人的税后薪资


'''
print('\n=====================运算工具==========================')
# 该函数是我们指定的一个运算法则


def after_sal(s):
    return s - (s - 3000) * 0.5


# 将df['salary]这个Series中的每个元素（薪资）作为参数
df['after_sal'] = df['salary'].map(after_sal)
print(df)


'''
- 数据分类处理的核心：

    - groupby()函数
    - groups属性查看分组情况

'''
print('\n=====================数据分类==========================')
df = pd.DataFrame(
    {
        'item': [
            'Apple', 'Banana', 'Orange', 'Banana', 'Orange', 'Apple'], 'price': [
                4, 3, 3, 2.5, 4, 2], 'color': [
                    'red', 'yellow', 'yellow', 'green', 'green', 'green'], 'weight': [
                        12, 20, 50, 30, 20, 44]})
print(df)
print('group by item')
print(df.groupby(['item']))
print('查看详细的分组')
print(df.groupby(['item']).groups)
print('分组聚合')

print('# 计算每一种水果的平均价格')
print(df.groupby(['item']).mean())
print(df.groupby(['item'])['price'].mean())
print('# 计算每一种颜色对于水果的平均重量')
print(df.groupby('color')['weight'].mean())
print('# 将计算出的平均重量汇总到源数据')
dic = df.groupby(by='color')['weight'].mean()  # mean()后可以加.to_dict()将输出结果转为字典
df['mean_weight'] = df['color'].map(dic)
print(df)


print('\n=====================高级数据聚合==========================')
'''
- 使用groupby分组后，也可以使用transform和apply提供自定义函数实现更多的运算
- df.groupby('item')['price'].sum() <==> df.groupby('item')['price'].apply(sum)
- transform和apply都会进行运算，在transform或者apply中传入函数即可
- transform和apply也可以传入一个lambda表达式

'''


def my_mean(s):
    m_sum = 0
    for i in s:
        m_sum += i
    return m_sum / len(s)


# transform 直接把计算后的值映射到源DataFrame，apply不会
print(df.groupby(by='item')['price'].transform(my_mean))
print(df.groupby(by='item')['price'].apply(my_mean))


print('\n=====================数据库操作==========================')
txt_file = pd.read_csv('./type-.txt', header=None, sep='-')
print(txt_file)
print(txt_file.shape)

print('\n读取数据库对象')
conn = sqlite3.connect('./weather_2012.sqlite')
sql_df = pd.read_sql('select * from weather_2012', conn)
print(sql_df)

# 将dataframe写入存储到db
# txt_file.to_sql('sql_txtfile', conn)

# 验证是否写入成功
sql_df2 = pd.read_sql('select * from sql_txtfile', conn)
print(sql_df2)


print('\n=====================透视表==========================')
'''
- 透视表是一种可以对数据动态排布并且分类汇总的表格格式。或许大多数人都在Excel使用过数据透视表，也体会到它的强大功能，而在pandas中它被称作pivot_table。
- 透视表的优点：
    - 灵活性高，可以随意定制你的分析计算要求
    - 脉络清晰易于理解数据
    - 操作性强，报表神器


#### pivot_table有四个最重要的参数index、values、columns、aggfunc
- index参数：分类汇总的分类条件
    - 每个pivot_table必须拥有一个index。如果想查看哈登对阵每个队伍的得分则需要对每一个队进行分类并计算其各类得分的平均值：
- values参数：需要对计算的数据进行筛选
    - 如果我们只需要哈登在主客场和不同胜负情况下的得分、篮板与助攻三项数据：
- Aggfunc参数：设置我们对数据聚合时进行的函数操作
    - 当我们未设置aggfunc时，它默认aggfunc='mean'计算均值。
- Columns:可以设置列层次字段
    - 对values字段进行分类

'''
df = pd.read_csv('./透视表-篮球赛.csv', encoding='utf8')
print(df)

print('# index为分类到条件')
print(df.pivot_table(index=['对手', '主客场']))
print('# 如果我们只需要哈登在主客场和不同胜负情况下的得分、篮板与助攻三项数据，默认是求得平均值，Aggfunc=mean')
print(df.pivot_table(index=['主客场', '胜负'], values=['得分', '篮板', '助攻']))
print('# 获得james harden在主客场和不同胜负情况下的总得分、总篮板、总助攻时')
print(
    df.pivot_table(
        index=[
            '主客场', '胜负'], values=[
                '得分', '篮板', '助攻'], aggfunc='sum'))

print('\n=====================交叉表==========================')
'''
- 是一种用于计算分组的特殊透视图,对数据进行汇总
- pd.crosstab(index,colums)
    - index:分组数据，交叉表的行索引
    - columns:交叉表的列索引


'''

df = pd.DataFrame(
    {
        'sex': [
            'man', 'man', 'women', 'women', 'man', 'women', 'man', 'women', 'women'], 'age': [
                15, 23, 25, 17, 35, 57, 24, 31, 22], 'smoke': [
                    True, False, False, True, True, False, False, True, False], 'height': [
                        168, 179, 181, 166, 173, 178, 188, 190, 160]})

print(df)
# 计算求出各个性别抽烟的个数
df2 = pd.crosstab(df.smoke, df.sex)
print(df2)
print(pd.crosstab(df.age, df.smoke))
