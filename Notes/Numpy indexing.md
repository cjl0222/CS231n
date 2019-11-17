## Numpy indexing

```python
import numpy as np

x = np.array([[1,  2],  
              [3,  4],  
              [5,  6]])
y = x[[0,1,2],  [0,1,0]]  
print (y)

'''
[1  4  5]
'''
```



```python
import numpy as np

x = np.array([[  0,  1,  2],
              [  3,  4,  5],
              [  6,  7,  8],
              [  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],
                 [3,3]])
cols = np.array([[0,2],
                 [0,2]])
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)

'''
我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]


这个数组的四个角元素是：
[[ 0  2]
 [ 9 11]]
'''
```

