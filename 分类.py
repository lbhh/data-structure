## 1



import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



df = pd.read_excel("example1.xlsx")



df  #有3个类别，a，ab，b



df = df.set_index(['类别'])  #将类别作为索引



df



df.at['a','横轴']   ##at是一种速度比loc、iloc、ix都快的查找方式



x = {1:'a',2:'ab',3:'b'}  #建立一个字典



for i in range(3):

    plt.plot(df.at[x[i+1],'横轴'],df.at[x[i+1],'纵轴'])



## 2





df = pd.read_excel("example.xlsx")





df[df['类别'] == 1]



for i in range(3):

    tmp = df[df['类别'] == (i+1)]

    plt.scatter(tmp['横轴'] , tmp['纵轴'])

plt.show()



#### 写成多重索引的形式并不能减少最外层索引的层数，因为没有办法对最外层直接引用，引用的其实是它所包含的许多行。
