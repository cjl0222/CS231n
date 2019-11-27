## Notes of Numpy Functions:



### numpy.sum():

```python
#example
import numpy as np
x = np.random.rand(2,3,4)    #生成三维随array
print("This is a 2*3rows 4cols array\n",x)
'''
>>> This is a 2*3rows 4cols array
[[[ 0.88264952  0.12446208  0.82166137  0.31747846]
  [ 0.51436626  0.03051283  0.46987831  0.64086531]
  [ 0.14819094  0.6395191   0.21753309  0.61340538]]

 [[ 0.0878878   0.5317064   0.65523138  0.704961  ]
  [ 0.51081521  0.88710145  0.92958269  0.89587262]
  [ 0.60233393  0.26146419  0.26584161  0.0823285 ]]]
'''
print('instance method:',x.sum())
print('numpy function:',np.sum(x))
'''
>>> 'instance method:', 11.835649415181807
>>> 'numpy function:', 11.835649415181807
'''

#对特定的轴求和
print('First axis sum',x.sum(axis=0))
'''
>>> 'First axis sum',   #第一维是轴0，对前后两页array加和得到3*4的array输出
array([[ 0.97053732,  0.65616848,  1.47689275,  1.02243946],
       [ 1.02518147,  0.91761428,  1.399461  ,  1.53673793],
       [ 0.75052486,  0.90098329,  0.4833747 ,  0.69573388]])
'''
print('Second axis sum',x.sum(axis=1))
'''
>>> 'Second axis sum',   #第二维是轴1，将每列的三行进行sum（对行求sum），得到2*4的输出
array([[ 1.54520672,  0.79449401,  1.50907277,  1.57174914],
       [ 1.20103694,  1.68027204,  1.85065568,  1.68316212]])
'''
print('Third axis sum',x.sum(axis=2))
'''
>>> 'Third axis sum',    #第三维是轴2，有4个数，将每行四个数加和（对列求sum），得到2*3输出
array([[ 2.14625142,  1.65562271,  1.6186485 ],
       [ 1.97978658,  3.22337197,  1.21196823]])
'''


#对多个轴求和
print('axis1,2 sum:',x.sum(axis=(1,2)))
'''
>>> 'axis1,2 sum:      #对第二维(axis=1)和第三维(axis=2)求和，归在第一维(axis=0)上
array([ 5.42052263,  6.41512678]) 
'''

```



### numpy.tile()

```python
    >>> a = np.array([0, 1, 2])
    >>> np.tile(a, 2)
    array([0, 1, 2, 0, 1, 2])
    >>> np.tile(a, (2, 2))
    array([[0, 1, 2, 0, 1, 2],
           [0, 1, 2, 0, 1, 2]])
    >>> np.tile(a, (2, 1, 2))
    array([[[0, 1, 2, 0, 1, 2]],
           [[0, 1, 2, 0, 1, 2]]])
    
    >>> b = np.array([[1, 2], [3, 4]])
    >>> np.tile(b, 2)
    array([[1, 2, 1, 2],
           [3, 4, 3, 4]])
    >>> np.tile(b, (2, 1))
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]])
    
    >>> c = np.array([1,2,3,4])
    >>> np.tile(c,(4,1))
    array([[1, 2, 3, 4],
           [1, 2, 3, 4],
           [1, 2, 3, 4],
           [1, 2, 3, 4]])
```



### About shape (2,) and (2,1)

一般情况下：

[1,2]的shape值(2,)，意思是一维数组，数组中有2个元素。

[[1],[2]]的shape值是(2,1)，意思是一个二维数组，每行有1个元素。

[[1,2]]的shape值是（1，2），意思是一个二维数组，每行有2个元素。



### numpy.array_split()

For an array of length l that should be split into n sections, it returns **l % n** sub-arrays of size **l//n + 1** and the rest of size **l//n**. 

 **前** `l % n` **个组的大小是** `l // n + 1`**，剩下组的大小是** `l // n`**。** 其中 `//` 表示下取整，即 `np.floor()`。 

Examples

```python
x = np.arange(8.0)
np.array_split(x, 3)
# [array([ 0.,  1.,  2.]), array([ 3.,  4.,  5.]), array([ 6.,  7.])]

x = np.arange(7.0)
np.array_split(x, 3)
# [array([ 0.,  1.,  2.]), array([ 3.,  4.]), array([ 5.,  6.])]

```

对于例子 1，`l` 为 8，`n` 为 3，前 `8 % 3 = 2` 个组的大小为 `8 // 3 + 1 = 3`，剩下组的大小为 `8 // 3 = 2`。

对于例子 2，`l` 为 7，`n` 为 3，前 `7 % 3 = 1` 个组的大小为 `7 // 3 + 1 = 3`，剩下组的大小为 `7 // 3 = 2`。



### numpy.hstack() 

 在水平方向上平铺 

```python

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print np.vstack((arr1,arr2))
'''
[[1 2 3]
 [4 5 6]]
'''

print np.hstack((arr1,arr2))
# [1 2 3 4 5 6] 

a1=np.array([[1,2],[3,4],[5,6]])
a2=np.array([[7,8],[9,10],[11,12]])

print a1
"""
[[1 2]
 [3 4]
 [5 6]]
"""

print a2
"""
[[ 7  8]
 [ 9 10]
 [11 12]]
"""

print np.hstack((a1,a2))
"""
[[ 1  2  7  8]
 [ 3  4  9 10]
 [ 5  6 11 12]]
"""
```



### numpy.argmax()

```python

import numpy as np
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
b=np.argmax(a, axis=0)#对二维矩阵来讲a[0][1]会有两个索引方向，第一个方向为a[0]，默认按列方向搜索最大值
#a的第一列为1，9，3,最大值为9，所在位置为1，
#a的第一列为5，6，7,最大值为7，所在位置为2，
#此此类推，因为a有4列，所以得到的b为1行4列，
print(b)#[1 2 2 1]
 
c=np.argmax(a, axis=1)#现在按照a[0][1]中的a[1]方向，即行方向搜索最大值，
#a的第一行为1，5，5，2,最大值为5（虽然有2个5，但取第一个5所在的位置），索引值为1，
#a的第2行为9，6，2，8,最大值为9，索引值为0，
#因为a有3行，所以得到的c有3个值，即为1行3列
print(c)#[1 0 2]

```

