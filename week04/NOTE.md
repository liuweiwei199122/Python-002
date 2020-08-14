学习笔记
练习数据处理的素材
from sklearn import datasets #引入数据集
# 鸢尾花数据集
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 查看特征
iris.feature_names

# 查看标签
iris.target_names

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)


# load_xxx 各种数据集
# load_boston Boston房屋价格 回归
# load_digits 手写体  分类
# load_iris   鸢尾花 分类聚类


import pandas as pd
import numpy as np
import matplotlib as plt
import os
pwd = os.path.dirname(os.path.realpath(__file__))   #获取文件绝对路径
book = os.path.join(pwd,'book_utf8.csv')
# df = pd.read_csv('book_utf8.csv')
df = pd.read_csv(book)
# 输出全部内容
print(df)

# 筛选标题为"还行"这一列
df['还行']

# 切片方式筛选
# 显示前3行
df[0:3]

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
df.loc[1:3, ['star']]

# 过滤数据
df['star'] == '力荐'
df [ df['star'] == '力荐' ]

# 缺失数据
df.dropna()

# 数据聚合
df.groupby('star').sum()

# 创建新列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df)

pandas数据类型：series和dataframe

series相当于excel中的一列，有行索引

dataframe相当于多行多列的excel表格，有行索引和列索引

数据导入

import pandas as pd

import numpy as np



# 从列表创建Series

pd.Series(['a', 'b', 'c'])

# 0    a

# 1    b

# 2    c

# dtype: object

# 自动创建索引



# 通过字典创建带索引的Series

s1 = pd.Series({'a':11, 'b':22, 'c':33})

# 通过关键字创建带索引的Series

s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])

s1

s2



# 获取全部索引

s1.index

# 获取全部值

s1.values



# 类型

type(s1.values)    # <class 'numpy.ndarray'>

type(np.array(['a', 'b']))



# 转换为列表

s1.values.tolist()



# 使用index会提升查询性能

#    如果index唯一，pandas会使用哈希表优化，查询性能为O(1)

#    如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)

#    如果index完全随机，每次查询都要扫全表，查询性能为O(N)



# 取出email

emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])

import re

pattern ='[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'

mask = emails.map(lambda x: bool(re.match(pattern, x)))

emails[mask]

import pandas as pd


# 列表创建dataframe
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# 嵌套列表创建dataframe
df2 = pd.DataFrame([
                     ['a', 'b'], 
                     ['c', 'd']
                    ])
# 自定义列索引
df2.columns= ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

df2
# 可以在创建时直接指定 DataFrame([...] , columns='...', index='...' )
# 查看索引
df2.columns, df2.index
type(df2.values)


import pandas as pd
# pip install xlrd
# 导入excel文件
excel1 = pd.read_excel(r'1.xlsx')
excel1
# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx',sheet_name = 0)

# 支持其他常见类型
pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')

pd.read_table( r'file.txt' , sep = ' ')

import pymysql
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)


# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
excel1.info()
excel1.describe()


import pandas as pd
import numpy as np

x = pd.Series([ 1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
#检验序列中是否存在缺失值
x.hasnans

# 将缺失值填充为平均值
x.fillna(value = x.mean())

# 前向填充缺失值

df3=pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
                 
df3.isnull().sum() # 查看缺失值汇总
df3.ffill() # 用上一行填充
df3.ffill(axis=1)  # 用前一列填充

# 缺失值删除
df3.info()
df3.dropna()

# 填充缺失值
df3.fillna('无')

# 重复值处理
df3.drop_duplicates()


import pandas as pd
# 行列调整
df = pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
# 列的选择,多个列要用列表
df[ ['A', 'C'] ]

# 某几列
df.iloc[:, [0,2]] # :表示所有行，获得第1和第3列

# 行选择
df.loc[ [0, 2] ] # 选择第1行和第3行
df.loc[ 0:2    ] # 选择第1行到第3行

# 比较
df[ ( df['A']<5 ) & ( df['C']<4 )   ]


# 数值替换

# 一对一替换
# 用于单个异常值处理
df['C'].replace(4,40)

import numpy as np
df.replace(np.NaN, 0)

# 多对一替换
df.replace([4,5,8], 1000)

# 多对多替换
df.replace({4:400,5:500,8:800})



# 排序
# 按照指定列降序排列
df.sort_values ( by = ['A'] ,ascending = False)

# 多列排序
df.sort_values ( by = ['A','C'] ,ascending = [True,False])


# 删除
# 删除列
df.drop( 'A' ,axis = 1)

# 删除行
df.drop( 3 ,axis = 0)

# 删除特定行
df [  df['A'] < 4 ]


# 行列互换
df.T
df.T.T

# 索引重塑
df4 = pd.DataFrame([
                     ['a', 'b', 'c'], 
                     ['d', 'e', 'f']
                    ],
                    columns= ['one', 'two', 'three'],
                    index = ['first', 'second']
                   )       
df4.stack()
df4.unstack()    
df4.stack().reset_index()             


import pandas as pd

df = pd.DataFrame({"A":[5,3,None,4], 

                 "B":[None,2,4,3], 

                 "C":[4,3,8,5], 

                 "D":[5,4,2,None]}) 

# 算数运算

# 两列之间的加减乘除

df['A'] + df['C'] 



# 任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值

df['A'] + 5



# 比较运算

df['A'] > df ['C']  



# count非空值计数

df.count()



# 非空值每列求和

df.sum()

df['A'].sum()



# mean求均值

# max求最大值

# min求最小值

# median求中位数  

# mode求众数

# var求方差

# std求标准差

import pandas as pd

import numpy as np



# 聚合

sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},

         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},

         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]



df2 = pd.DataFrame(sales)

df2.groupby('type').groups



for a, b in df2.groupby('type'):

    print(a)

    print(b)



# 聚合后再计算

df2.groupby('type').count()

# df2.groupby('Jan').sum()





# 各类型产品的销售数量和销售总额

df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' })





group=['x','y','z']

data=pd.DataFrame({

    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,

    "salary":np.random.randint(5,50,10),

    "age":np.random.randint(15,50,10)

    })





data.groupby('group').agg('mean')

data.groupby('group').mean().to_dict()

data.groupby('group').transform('mean')



# 数据透视表

pd.pivot_table(data, 

               values='salary', 

               columns='group', 

               index='age', 

               aggfunc='count', 

               margins=True  

            ).reset_index()


import pandas as pd

import numpy as np



group = ['x','y','z']

data1 = pd.DataFrame({

    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,

    "age":np.random.randint(15,50,10)

    })



data2 = pd.DataFrame({

    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,

    "salary":np.random.randint(5,50,10),

    })



data3 = pd.DataFrame({

    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,

    "age":np.random.randint(15,50,10),

    "salary":np.random.randint(5,50,10),

    })



# 一对一

pd.merge(data1, data2)



# 多对一

pd.merge(data3, data2, on='group')



# 多对多

pd.merge(data3, data2)



# 连接键类型，解决没有公共列问题

pd.merge(data3, data2, left_on= 'age', right_on='salary')



# 连接方式

# 内连接，不指明连接方式，默认都是内连接

pd.merge(data3, data2, on= 'group', how='inner')

# 左连接 left

# 右连接 right

# 外连接 outer



# 纵向拼接

pd.concat([data1, data2])


# 导出为.xlsx文件

df.to_excel( excel_writer = r'file.xlsx')



# 设置Sheet名称

df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1')



# 设置索引,设置参数index=False就可以在导出时把这种索引去掉

df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', index = False)



# 设置要导出的列

df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', 

             index = False, columns = ['col1','col2'])



# 设置编码格式

enconding = 'utf-8'



# 缺失值处理

na_rep = 0 # 缺失值填充为0



# 无穷值处理

inf_rep = 0



# 导出为.csv文件

to_csv()



# 性能

df.to_pickle('xx.pkl') 



agg(sum) # 快

agg(lambda x: x.sum()) # 慢


import pandas as pd

import numpy as np



dates = pd.date_range('20200101', periods=12)

df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))

df



#                    A         B         C         D

# 2020-01-01  0.046485 -0.556209  1.062881 -1.174129

# 2020-01-02  1.066051 -0.343081  1.054913  1.601051

# 2020-01-03  0.191064 -0.386905  0.516403  0.259818

# 2020-01-04 -0.168462 -1.488041 -0.457658  0.913574

# 2020-01-05 -0.502614  1.235633 -0.578284 -0.362737

# 2020-01-06 -0.193310  0.652285 -0.346359  0.347364

# 2020-01-07  2.308562 -0.679108  0.856449  0.490840

# 2020-01-08  0.871489  0.338133 -0.163669  0.300147

# 2020-01-09 -1.245250  0.667357 -1.287782  1.494880

# 2020-01-10  0.387925 -1.058867 -0.397298  0.514921

# 2020-01-11 -0.440884  0.904307  1.338720  0.612919

# 2020-01-12 -0.864941 -0.358934 -0.203868 -1.191186



import matplotlib.pyplot as plt

plt.plot(df.index, df['A'], )

plt.show()



plt.plot(df.index, df['A'], 

        color='#FFAA00',    # 颜色

        linestyle='--',     # 线条样式

        linewidth=3,        # 线条宽度

        marker='D')         # 点标记



plt.show()



# seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观

import seaborn as sns

# 绘制散点图

plt.scatter(df.index, df['A'])

plt.show()



# 美化plt

sns.set_style('darkgrid')

plt.scatter(df.index, df['A'])

plt.show()


