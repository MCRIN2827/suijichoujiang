# Lucky Draw


Lucky Draw is a program for selecting a few lucky dogs from a group of people.
## Installation


Copy the Python codes.
```python
from random import randint
All = raw_input('请输入参与抽奖总人数:')
Num = raw_input('请输入需要抽奖个数:')
flag = True

while flag:
    if Num.isdigit() and All.isdigit():
        Ind1 = int(Num)
        Ind2 = int(All)
        flag = False
    else:
        print '输入错误'
        break
else:
    for i in range(Ind1):
        print randint(1,Ind2)    
```
##Usage


Input the number of people and then input the number of lucky dogs.  


![](QQ图片20200811102535.png)
## Contributing


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
