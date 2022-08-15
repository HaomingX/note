### numpy

```python
import numpy as np
```

### 把列表转换成矩阵的方法 [][]是列表

```python
array =np.array([[1,2,3],[2,3,4]])  # 把列表转换成矩阵的方法 [][]是列表
print(array)
[[1 2 3]
 [2 3 4]]
```

### 查看维度

```python
print('number of dim:',array.ndim)  # 查看维度
number of dim: 2
```

### 查看形状

```python
print('shape:',array.shape)  # 查看形状
shape: (2, 3)
```

### 查看一共有多少元素

```python
print('size:',array.size)  # 查看一共有多少元素
size: 6
```

### 定义type int32 float32 float64

```python
a = np.array([[1,2,3],
               [2,3,4]
             ],
             dtype=np.int)  # 定义type  int32 float32 float64
print(a.dtype)
int64
```

### 生成全部为0的矩阵

```python
a = np.zeros((3,4))  # 生成全部为0的矩阵
a
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

### 全部为1的矩阵

```python
a = np.ones((3,4), dtype=np.int16)  # 全部为1的矩阵
a
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]], dtype=int16)
```

### 全部为空的

```python
a = np.empty((3,4))  # 全部为空的
a
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

### 生成有序的矩阵 起始值，终止值，步长

```python
a = np.arange(10,20,2)  # 生成有序的矩阵 起始值，终止值，步长
a
array([10, 12, 14, 16, 18])
```

### 生成有序的三行四列

```python
a = np.arange(12).reshape((3,4))  # 生成有序的三行四列
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

### 生成线段

```python
a = np.linspace(1, 10, 5)  # 生成线段
a
array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ])
```

### 改形状，但是注意6 = 2*3

```python
a = np.linspace(1, 10, 6).reshape((2,3))  #改形状，但是注意6 = 2*3
a
array([[ 1. ,  2.8,  4.6],
       [ 6.4,  8.2, 10. ]])
a = np.array([10,20,30,40])
b = np.arange(4)
```

### 减法

```python
c = a - b  # 减法
c
array([10, 19, 28, 37])
```

### 加法

```python
c = a + b  # 加法
c
array([10, 21, 32, 43])
```

### 乘法

```python
c = a * b  # 乘法
c
array([  0,  20,  60, 120])
```

### 平方

```python
c = b ** 2  # 平方
c
array([0, 1, 4, 9])
```

### 求三角函数

```python
c = 10 * np.sin(a)  # 求三角函数
c
array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
```

### 找出矩阵中小于某值的数

```python
print(b<3)  # 找出矩阵中小于某值的数
[ True  True  True False]
```

### 矩阵乘法

```python
a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape(2,2)
a
array([[1, 1],
       [0, 1]])
b
array([[0, 1],
       [2, 3]])
#### 逐个相乘
c = a * b
c
array([[0, 1],
       [0, 3]])
```

### 矩阵乘法(两种写法)

```python
c = np.dot(a,b)
c
array([[2, 4],
       [2, 3]])
c_1 = a.dot(b)
c_1
array([[2, 4],
       [2, 3]])
```

### 随机产生

```python
a = np.random.random((2,4))
a
array([[0.08518757, 0.48170131, 0.83449221, 0.03569221],
       [0.96323027, 0.73438721, 0.41844926, 0.98153234]])
```

### 最大，最小，求和

```python
np.sum(a)
np.min(a)
np.max(a)
0.9815323368363336
```

### 求和的维度 axis=0 列 axis = 1 行

```python
np.sum(a, axis=0)
array([1.04841785, 1.21608852, 1.25294146, 1.01722455])
A = np.arange(2, 14).reshape((3,4))
A
array([[ 2,  3,  4,  5],
       [ 6,  7,  8,  9],
       [10, 11, 12, 13]])
```

### 一些小函数

```python
print(np.argmin(A))
0
np.argmax(A)
np.mean(A)  # A.mean() 也可以
np.average(A)  # A.average不行
np.median(A)  # 中位数
np.cumsum(A)  # 累加
np.diff(A)  # 差
np.nonzero(A)  # 非0的数  输出对应每个位置 一个array行 一个array列
np.sort(A)  # 排序
np.transpose(A)  # 矩阵反向,转置  A.T
np.clip(A, 5, 9)  # 小于5的=5，大于9的变成9
A.flatten()  # 放平
A.flat  # 迭代器
<numpy.flatiter at 0x7fb4b6820600>
```

### 根据索引找

```python
A = np.arange(3,15).reshape(3,4)
A
array([[ 3,  4,  5,  6],
       [ 7,  8,  9, 10],
       [11, 12, 13, 14]])
print(A[2])  # 索引为2
[11 12 13 14]
print(A[2,2])  # 索引为2,2
13
print(A[2,:])  # 行索引为2的所有
[11 12 13 14]
for row in A:  # 迭代行
    print(row)
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
for column in A.T:  # 迭代列  trick的方法
    print(column)
[ 3  7 11]
[ 4  8 12]
[ 5  9 13]
[ 6 10 14]
for item in A.flat:  # 迭代项目
    print(item)
3
4
5
6
7
8
9
10
11
12
13
14
print(A.flatten())
[ 3  4  5  6  7  8  9 10 11 12 13 14]
```

### 合并

```python
A = np.array([1,1,1])
B = np.array([2,2,2])
```

### 上下合并

```python
print(np.vstack((A,B)))  # vertica stack 注意传tuple 可以合并多个
[[1 1 1]
 [2 2 2]]
```

### 左右合并

```python
print(np.hstack((A,B)))
[1 1 1 2 2 2]
```

### 加维度

```python
print(A[np.newaxis,:].shape)
C = A[:,np.newaxis]
(1, 3)
print(A[:,np.newaxis].shape)
D = A[:,np.newaxis]
(3, 1)
```

### 多个矩阵合并

```python
print(np.concatenate((C,D,C,D), axis=1))
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
```

### 分割数组

```python
A = np.arange(12).reshape((3,4))
print(A)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
print(np.split(A, 2, axis=1))  # 从行进行分割
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
print(np.split(A, 3,axis=0))  # 从列进行分割
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
```

### 不等量分割

```python
print(np.array_split(A,3,axis=1))
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2],
       [ 6],
       [10]]), array([[ 3],
       [ 7],
       [11]])]
print(np.vsplit(A,3))  # 纵向分割
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(A,2))  # 横向分割
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
```

### 赋值

```python
a = np.arange(4)
a
array([0, 1, 2, 3])
b = a  # 赋值
c = a
d = b
a[0] = 11   # 改变a中的值
b  # 全变了  是个引用改变
array([11,  1,  2,  3])
b is a  # b 就是 a
True
d is a  # d也是a
True
d[1:3] = [22, 33]
a  # a也改变了
array([11, 22, 33,  3])
```

### 赋值但是不关联

```python
b = a.copy()  # deep copy
b
array([11, 22, 33,  3])
a[3] = 44
b  # 没有改变
array([11, 22, 33,  3])
```

### pandas

```python
import pandas as pd
import numpy as np
```

### 序列

```python
s = pd.Series([1,2,3,7,np.nan,44,1])
s
0     1.0
1     2.0
2     3.0
3     7.0
4     NaN
5    44.0
6     1.0
dtype: float64
```

### 日期序列

```python
date = pd.date_range('20191026',periods=6)
date
DatetimeIndex(['2019-10-26', '2019-10-27', '2019-10-28', '2019-10-29',
               '2019-10-30', '2019-10-31'],
              dtype='datetime64[ns]', freq='D')
```

### 定义行索引

```python
df = pd.DataFrame(np.random.randn(6,4), index=date,columns=['a','b','c','d'])
df
```

a b c d 2019-10-26 -0.530462 -0.138865 -0.986850 0.202214 2019-10-27 0.260291 -0.253043 -0.081724 -1.068172 2019-10-28 -0.277169 -0.173014 -1.057266 -0.369085 2019-10-29 1.916745 0.062108 -1.024847 -0.166449 2019-10-30 -1.555946 -1.197340 -2.393859 0.291020 2019-10-31 -0.738532 1.031493 -1.670829 0.496059

```python
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
df1
```

0 1 2 3 0 0 1 2 3 1 4 5 6 7 2 8 9 10 11

```python
df2 = pd.DataFrame({'A':1.,
                   'B':pd.Timestamp('20191026'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'
                   })
df2
```

A B C D E F 0 1.0 2019-10-26 1.0 3 test foo 1 1.0 2019-10-26 1.0 3 train foo 2 1.0 2019-10-26 1.0 3 test foo 3 1.0 2019-10-26 1.0 3 train foo

### 查数据类型

```python
df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```

### 查列

```python
df2.index
Int64Index([0, 1, 2, 3], dtype='int64')
```

### 查行

```python
df2.columns
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
```

### 查value

```python
df2.values
array([[1.0, Timestamp('2019-10-26 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2019-10-26 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2019-10-26 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2019-10-26 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
```

### 查数据的大纲

```python
df2.describe()  # 但是只能运算数字的
```

A C D count 4.0 4.0 4.0 mean 1.0 1.0 3.0 std 0.0 0.0 0.0 min 1.0 1.0 3.0 25% 1.0 1.0 3.0 50% 1.0 1.0 3.0 75% 1.0 1.0 3.0 max 1.0 1.0 3.0

### 转置

```python
df2.T
```

0 1 2 3 A 1 1 1 1 B 2019-10-26 00:00:00 2019-10-26 00:00:00 2019-10-26 00:00:00 2019-10-26 00:00:00 C 1 1 1 1 D 3 3 3 3 E test train test train F foo foo foo foo

### 排序

```python
df2.sort_index(axis=1,ascending=False)  # 倒序排列，以行为索引
```

F E D C B A 0 foo test 3 1.0 2019-10-26 1.0 1 foo train 3 1.0 2019-10-26 1.0 2 foo test 3 1.0 2019-10-26 1.0 3 foo train 3 1.0 2019-10-26 1.0

```python
df2.sort_values(by='E')  # 以行排序
```

A B C D E F 0 1.0 2019-10-26 1.0 3 test foo 2 1.0 2019-10-26 1.0 3 test foo 1 1.0 2019-10-26 1.0 3 train foo 3 1.0 2019-10-26 1.0 3 train foo

### 选择数据

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
```

### 选一列

```python
print(df['A'], df.A)
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int64 2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int64
```

### 选几行

```python
print(df[0:3], df['20130102':'20130104'])
A  B   C   D
2013-01-01  0  1   2   3
2013-01-02  4  5   6   7
2013-01-03  8  9  10  11              A   B   C   D
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
```

### 选label

```python
print(df.loc['20130102'])
A    4
B    5
C    6
D    7
Name: 2013-01-02 00:00:00, dtype: int64
```

### 选label和行

```python
print(df.loc[:,['A','B']])
A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
```

### 位置筛选

```python
print(df.iloc[3])
A    12
B    13
C    14
D    15
Name: 2013-01-04 00:00:00, dtype: int64
```

### 第几行第几个

```python
print(df.iloc[3,1])
13
```

### 切片

```python
print(df.iloc[3:5, 1:3])
B   C
2013-01-04  13  14
2013-01-05  17  18
print(df.iloc[[1,3,5], 1:3])
B   C
2013-01-02   5   6
2013-01-04  13  14
2013-01-06  21  22
```

### 标签和数字都可筛选 混合筛选

```python
print(df.ix[:3,['A','C']])
A   C
2013-01-01  0   2
2013-01-02  4   6
2013-01-03  8  10


/Users/shinkeika/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated
  """Entry point for launching an IPython kernel.
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/pandas/core/indexing.py:822: FutureWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated
  retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
```

### 条件筛选

```python
print(df[df.A > 8])
A   B   C   D
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
```

### 设置值

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df
```

A B C D 2013-01-01 0 1 2 3 2013-01-02 4 5 6 7 2013-01-03 8 9 10 11 2013-01-04 12 13 14 15 2013-01-05 16 17 18 19 2013-01-06 20 21 22 23

```python
df.iloc[2,2] = 1111
df
```

A B C D 2013-01-01 0 1 2 3 2013-01-02 4 5 6 7 2013-01-03 8 9 1111 11 2013-01-04 12 13 14 15 2013-01-05 16 17 18 19 2013-01-06 20 21 22 23

```python
df.loc['20130101', 'B'] = 2222
df
```

A B C D 2013-01-01 0 2222 2 3 2013-01-02 4 5 6 7 2013-01-03 8 9 1111 11 2013-01-04 12 13 14 15 2013-01-05 16 17 18 19 2013-01-06 20 21 22 23

```python
df[df.A > 4] = 0  # A大于4的所有行都0
df
```

A B C D 2013-01-01 0 2222 2 3 2013-01-02 4 5 6 7 2013-01-03 0 0 0 0 2013-01-04 0 0 0 0 2013-01-05 0 0 0 0 2013-01-06 0 0 0 0

```python
df.A[df.A > 4] = 0  # A大于4的A行都0
df
```

A B C D 2013-01-01 0 2222 2 3 2013-01-02 4 5 6 7 2013-01-03 0 0 0 0 2013-01-04 0 0 0 0 2013-01-05 0 0 0 0 2013-01-06 0 0 0 0

### 加一列

```python
df['F'] = np.nan
df
```

A B C D F 2013-01-01 0 2222 2 3 NaN 2013-01-02 4 5 6 7 NaN 2013-01-03 0 0 0 0 NaN 2013-01-04 0 0 0 0 NaN 2013-01-05 0 0 0 0 NaN 2013-01-06 0 0 0 0 NaN

```python
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101',periods=6))
df
```

A B C D F E 2013-01-01 0 2222 2 3 NaN 1 2013-01-02 4 5 6 7 NaN 2 2013-01-03 0 0 0 0 NaN 3 2013-01-04 0 0 0 0 NaN 4 2013-01-05 0 0 0 0 NaN 5 2013-01-06 0 0 0 0 NaN 6

### 处理丢失数据

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
df
```

A B C D 2013-01-01 0 NaN 2.0 3 2013-01-02 4 5.0 NaN 7 2013-01-03 8 9.0 10.0 11 2013-01-04 12 13.0 14.0 15 2013-01-05 16 17.0 18.0 19 2013-01-06 20 21.0 22.0 23

### 丢掉一行或者一列

```python
print(df.dropna(axis=0,how='any'))  # how=['any','all']  axis=0丢行  all是全为0 才丢
A     B     C   D
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
print(df.fillna(value=0))
A     B     C   D
2013-01-01   0   0.0   2.0   3
2013-01-02   4   5.0   0.0   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
```

### 是否丢失数据

```python
print(df.isnull())
A      B      C      D
2013-01-01  False   True  False  False
2013-01-02  False  False   True  False
2013-01-03  False  False  False  False
2013-01-04  False  False  False  False
2013-01-05  False  False  False  False
2013-01-06  False  False  False  False
```

### 是否丢失

```python
print(np.any(df.isnull()) == True)
True
```

### 储存，导出导出

```python
import pandas as pd
data = pd.read_csv('student.csv')
data
```

Student ID name age gender 0 1100 Kelly 22 Female 1 1101 Clo 21 Female 2 1102 Tilly 22 Female 3 1103 Tony 24 Male 4 1104 David 20 Male 5 1105 Catty 22 Female 6 1106 M 3 Female 7 1107 N 43 Male 8 1108 A 13 Male 9 1109 S 12 Male 10 1110 David 33 Male 11 1111 Dw 3 Female 12 1112 Q 23 Male 13 1113 W 21 Female

```python
data.to_pickle('student.pickle')
```

### 合并

```python
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((3,4)) * 0 ,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4)) * 1 ,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4)) * 2 ,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
```

### 上下合并

```python
res = pd.concat([df1,df2,df3], axis=0, ignore_index=True)  # axis=0 是竖向的 ignore_index重建索引
res
```

a b c d 0 0.0 0.0 0.0 0.0 1 0.0 0.0 0.0 0.0 2 0.0 0.0 0.0 0.0 3 1.0 1.0 1.0 1.0 4 1.0 1.0 1.0 1.0 5 1.0 1.0 1.0 1.0 6 2.0 2.0 2.0 2.0 7 2.0 2.0 2.0 2.0 8 2.0 2.0 2.0 2.0

```python
df1 = pd.DataFrame(np.ones((3,4)) * 0 ,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4)) * 0 ,columns=['b','c','d','e'])
print(df1)
print(df2)
a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     b    c    d    e
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
```

### 覆盖合并 （不去重）

```python
res = pd.concat([df1, df2], join='outer')  # 默认是outer
res
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

  """Entry point for launching an IPython kernel.
```

a b c d e 0 0.0 0.0 0.0 0.0 NaN 1 0.0 0.0 0.0 0.0 NaN 2 0.0 0.0 0.0 0.0 NaN 0 NaN 0.0 0.0 0.0 0.0 1 NaN 0.0 0.0 0.0 0.0 2 NaN 0.0 0.0 0.0 0.0

### 覆盖合并（去重）

```python
res = pd.concat([df1, df2], join='inner',ignore_index=True)  # 默认是outer
res
```

b c d 0 0.0 0.0 0.0 1 0.0 0.0 0.0 2 0.0 0.0 0.0 3 0.0 0.0 0.0 4 0.0 0.0 0.0 5 0.0 0.0 0.0

### join_axes 只考虑第几个索引

```python
df1 = pd.DataFrame(np.ones((3,4)) * 0 ,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4)) * 1 ,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)
a    b    c    d
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  0.0  0.0  0.0  0.0
     b    c    d    e
2  1.0  1.0  1.0  1.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])  #只考虑1的索引
res
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: The join_axes-keyword is deprecated. Use .reindex or .reindex_like on the result to achieve the same functionality.
  """Entry point for launching an IPython kernel.
```

a b c d b c d e 1 0.0 0.0 0.0 0.0 NaN NaN NaN NaN 2 0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0 3 0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0

```python
res = pd.concat([df1,df2],axis=1)
res
```

a b c d b c d e 1 0.0 0.0 0.0 0.0 NaN NaN NaN NaN 2 0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0 3 0.0 0.0 0.0 0.0 1.0 1.0 1.0 1.0 4 NaN NaN NaN NaN 1.0 1.0 1.0 1.0

### append

```python
df1 = pd.DataFrame(np.ones((3,4)) * 0 ,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4)) * 1 ,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4)) * 2 ,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
     a    b    c    d
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
res = df1.append([df2,df3],ignore_index=True)
res
```

a b c d 0 0.0 0.0 0.0 0.0 1 0.0 0.0 0.0 0.0 2 0.0 0.0 0.0 0.0 3 1.0 1.0 1.0 1.0 4 1.0 1.0 1.0 1.0 5 1.0 1.0 1.0 1.0 6 2.0 2.0 2.0 2.0 7 2.0 2.0 2.0 2.0 8 2.0 2.0 2.0 2.0

### 添加series

```python
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)
res
```

a b c d 0 0.0 0.0 0.0 0.0 1 0.0 0.0 0.0 0.0 2 0.0 0.0 0.0 0.0 3 1.0 2.0 3.0 4.0

### 合并merge

```python
import pandas as pd
import numpy as np
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
res = pd.merge(left,right,on='key')  # 基于key来合并
res
```

key A B C D 0 K0 A0 B0 C0 D0 1 K1 A1 B1 C1 D1 2 K2 A2 B2 C2 D2 3 K3 A3 B3 C3 D3

```python
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
key1 key2   A   B
0   K0   K0  A0  B0
1   K1   K1  A1  B1
2   K2   K0  A2  B2
3   K3   K1  A3  B3
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K2   K0  C2  D2
3   K3   K0  C3  D3
res = pd.merge(right,left,on=['key1','key2'],how='outer')  # 两个都考虑, 默认inner会去重
                                                        # 基于right 基于left都可以
res
```

key1 key2 C D A B 0 K0 K0 C0 D0 A0 B0 1 K1 K0 C1 D1 NaN NaN 2 K2 K0 C2 D2 A2 B2 3 K3 K0 C3 D3 NaN NaN 4 K1 K1 NaN NaN A1 B1 5 K3 K1 NaN NaN A3 B3

```python
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res = pd.merge(df1, df2 ,on='col1',how='outer',indicator=True)
res
col1 col_left
0     0        a
1     1        b
   col1  col_right
0     1          2
1     2          2
2     2          2
```

col1 col_left col_right _merge 0 0 a NaN left_only 1 1 b 2.0 both 2 2 NaN 2.0 right_only 3 2 NaN 2.0 right_only

### merged by index

```python
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                                  'B': ['B0', 'B1', 'B2']},
                                  index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                                     'D': ['D0', 'D2', 'D3']},
                                      index=['K0', 'K2', 'K3'])
print(left)
print(right)
A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
res
```

A B C D K0 A0 B0 C0 D0 K1 A1 B1 NaN NaN K2 A2 B2 C2 D2 K3 NaN NaN C3 D3

```python
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
res
```

A B C D K0 A0 B0 C0 D0 K2 A2 B2 C2 D2

### handle overlapping

```python
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
k  age_boy  age_girl
0  K0        1         4
1  K0        1         5
```

### pandas画图

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:211: RuntimeWarning: Glyph 8722 missing from current font.
  font.set_text(s, 0.0, flags=flags)
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:180: RuntimeWarning: Glyph 8722 missing from current font.
  font.set_text(s, 0, flags=flags)
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-ca13614baec854f07372abdf98977c65_1440w.jpg)



```python
data = pd.DataFrame(np.random.randn(1000,4),
                   index=np.arange(1000),
                    columns=list('ABCD')
                   )
data.head()
```

A B C D 0 -1.524434 0.228077 -0.176696 0.078439 1 0.495711 1.511561 -1.933811 -0.963600 2 0.776679 -0.483186 0.833599 0.687600 3 0.163510 0.838325 0.332801 0.663812 4 0.355118 -0.800993 -1.585355 0.896179

```python
data = data.cumsum()
data.plot()
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-91babd6f0a7097b79b7ef333c5e11ee0_1440w.jpg)



```python
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = data.plot.scatter(x='A', y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2', ax=ax)  #把ax赋值到第二个上,ax代表第一个窗口
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-ae95b694e86c3d486a7969d2d6f70d19_1440w.jpg)



### Matplotlib

### plot图形

```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,50)  # 生成线段
y = 2 * x + 1
plt.plot(x,y)
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-ba787c8b628d77d9e4cb426b92b192e2_1440w.jpg)



### figure的使用

```python
x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1)
plt.figure(num = 3,figsize=(8,5))  # num 为序号
plt.plot(x, y2)
plt.plot(x, y1,color='red', linewidth=1.0, linestyle='--')  # 可以在一个figure画两个
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-976b91f46493df5e6ceb844aed54278a_1440w.jpg)





![img](https://pic3.zhimg.com/v2-c552d3989b807a67d29e23548ed3c99a_r.jpg)



### 修改坐标轴

```python
plt.xlim((-1,2))
plt.ylim((3,-2))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  # 换脚标
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ good$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
            # 一一对应，$是为了换字体   \ 是在$里转置字符   \alpha是为了显示alpha
([<matplotlib.axis.YTick at 0x11b2509b0>,
  <matplotlib.axis.YTick at 0x11b20e080>,
  <matplotlib.axis.YTick at 0x11b2f2e48>,
  <matplotlib.axis.YTick at 0x11b2310f0>,
  <matplotlib.axis.YTick at 0x118ece588>],
 <a list of 5 Text yticklabel objects>)
```



![img](https://pic2.zhimg.com/v2-7ff2e34d2bfb06a343b5987b21862b59_r.jpg)



### 设置坐标轴(位置)

```python
plt.xlim((-1,2))
plt.ylim((3,-2))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  # 换脚标
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ good$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
            # 一一对应，$是为了换字体   \ 是在$里转置字符   \alpha是为了显示alpha


# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')  # spines代表四个边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))  # 通过data来选择位置 是 0 的时候为坐标远点  axes是指比例到多少的时候
ax.spines['left'].set_position(('data', 0))
```



![img](https://pic3.zhimg.com/80/v2-9de868b9d82817468d245eb5279aaf2e_1440w.jpg)



### 图例

```python
plt.xlim((-1,2))
plt.ylim((3,-2))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  # 换脚标
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ good$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
            # 一一对应，$是为了换字体   \ 是在$里转置字符   \alpha是为了显示alpha
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(handles=[l1, l2], labels=['aaa','bbb'], loc='upper right')  # loc 可以选best.  
# 如果handles接东西，前提，接的东西是加点的形式
plt.show()
```



![img](https://pic4.zhimg.com/v2-4e2dbc431c18828128c6426f14da9aff_r.jpg)



### 注解

```python
x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)  # k代表黑色 black  [x0,0][x0,y0]两个点 黑色虚线
plt.scatter([x0, ], [y0, ], s=50, color='b')
# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))  # xy代表哪个点，xytext基于x0 y0什么位置开始打印字
Text(30, -30, '$2x+1=3$')
```



![img](https://pic1.zhimg.com/v2-6d383608c16b72d0653a66738f55fb10_r.jpg)



```python
x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)  # k代表黑色 black  [x0,0][x0,y0]两个点 黑色虚线
plt.scatter([x0, ], [y0, ], s=50, color='b')
# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))  # xy代表哪个点，xytext基于x0 y0什么位置开始打印字

# method 2
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 15, 'color': 'r'})
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-556ef67ec9e01c8c82d202fc2594d010_r.jpg)



### tick能见度

```python
x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)      # set zorder for ordering the plot in plt 2.0.2 or higher
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-fb317a95274d6f644d64d863560e8aaf_1440w.jpg)



### 散点图plot

```python
n = 1024
X = np.random.normal(0, 1, n) 
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # 颜色
# plt.scatter(X,Y, s=75,c=T,alpha=0.5)
plt.scatter(np.arange(5),np.arange(5))
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
plt.xticks(())  # 传空，代表把刻度去掉
plt.yticks(())
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-9e26dafa86f4d7eabbdb60e2081d7818_1440w.jpg)



### 柱状图

```python
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y1, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):  # 把X，Y1分别传给 x,y
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')  # ha= harizontal alignment


for x,y in zip(X,Y2):  # 把X，Y2分别传给 x,y
    plt.text(x + 0.4, -(y + 0.05), '-%.2f' % y, ha='center', va='top')  # ha= harizontal alignment

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-9de42da7ee888b141436676472523a76_1440w.jpg)



### 等高线

```python
def f(x,y):
    # the height function
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 10, alpha=0.75,cmap=plt.cm.hot)  # cmap 是数值和颜色的对应
# use plt.contour to add contour lines
C = plt.contour(X, Y,f(X,Y), 10, colors='black', linewidth=.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)  # inline 表示线不会穿过数字

plt.xticks(())
plt.yticks(())
plt.show()
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:10: UserWarning: The following kwargs were not used by contour: 'linewidth'
  # Remove the CWD from sys.path while we load stuff.
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-10a244d0400caf3c30b14b277a14c16e_1440w.jpg)



### 打印图像

```python
import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
a
array([[0.31366083, 0.36534842, 0.42373312],
       [0.36534842, 0.43959993, 0.52508375],
       [0.42373312, 0.52508375, 0.65153635]])
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper') # origin 就是高在上，低在上的设置
# interpolation 表示不同的展示类型
plt.colorbar(shrink=0.9)  # shrink是表示和原图的比例
plt.xticks()
plt.yticks()
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-6351bc40f3347b87ec072f62037d5890_1440w.jpg)



### 3D图像

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D坐标轴的显示

fig = plt.figure()
ax = Axes3D(fig)


X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X,Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)

Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cmap=plt.get_cmap('rainbow'))  # rstride,cstride 表示跨度是多少 c=color r=row

ax.contourf(X, Y, Z, zdir='x', offset=-4, cmap='rainbow')  # 等高线图 zdir = zdirection 表示把等高线图放到什么位置  offset表示压到那个值的平面

plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-f3d0f97dcb9433d0b4d6e5e52d35d667_r.jpg)



### subplot多个图

```python
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2, 2, 1)  # 分成两行两列  1代表第一张图
plt.plot([0,1],[0,1])

plt.subplot(2, 2, 2)  # 分成两行两列  2 第二张
plt.plot([0,1],[0,2])

plt.subplot(2, 2, 3)  # 分成两行两列  
plt.plot([0,1],[0,3])

plt.subplot(2, 2, 4)  # 分成两行两列  
plt.plot([0,1],[0,4])

plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-ca3b886788859515cbe0952cc3862db7_1440w.jpg)



```python
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2, 1, 1)  # 分成两行两列  第一个1代表分成几个column 1代表第一张图 
plt.plot([0,1],[0,1])

plt.subplot(2, 3, 4)  # 分成两行两列  2 第二张   第二列分三个column
plt.plot([0,1],[0,2])

plt.subplot(2, 3, 5)  # 分成两行两列  
plt.plot([0,1],[0,3])

plt.subplot(2, 3, 6)  # 分成两行两列  
plt.plot([0,1],[0,4])

plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-559d6eb8bd14d827a3b89b6c851352de_1440w.jpg)



### 多个图

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# method 1
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes #整个grid代表3行3列，第一个从0，0开始。colspan是指跨几列
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)  # 索引是从0.0开始，1，0代表索引下移一位。
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)  # 索引右移2
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-e10f7eb86ff9c5320f2159147eaf08d0_1440w.jpg)



```python
# method 2
plt.figure()
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, 1])
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-e1147303c90f52293659e37d601840cb_1440w.jpg)



```python
# method 3
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

plt.tight_layout()
plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-6a4f4be631e10af5f2f02a26c77d2a44_r.jpg)



### 图中图

```python
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
<Figure size 432x288 with 0 Axes>
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  # 是占整个图的百分比
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')


# # different method to add axes
# ####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')  # y倒序
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-dad5250d1691fe6ce907e176dfaaacc9_1440w.png)



### 次坐标轴

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 *y1

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()    # mirror the ax1
ax1.plot(x, y1, 'g-')  # 实线
ax2.plot(x, y2, 'b--')  # 虚线

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')

plt.show()
```



![img](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/v2-f0b1b69058b848c4d7904c61f30bf883_1440w.jpg)



### 动画

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # 逗号是 只要反回的第一个。

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)  # func更新数据，init_func初始是什么样的,blit 表示是否全部更新整个图片

plt.show()
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:211: RuntimeWarning: Glyph 8722 missing from current font.
  font.set_text(s, 0.0, flags=flags)
/Users/shinkeika/anaconda3/lib/python3.7/site-packages/matplotlib/backends/backend_agg.py:180: RuntimeWarning: Glyph 8722 missing from current font.
  font.set_text(s, 0, flags=flags)
```

![img](https://pic3.zhimg.com/80/v2-a02db3dd11b4282425fddf7cb8ee3546_1440w.jpg)