from time import ctime
from decimal import Decimal

# print the time
print('Time: %s\n'%ctime())

# loop1:while
print('----------loop1----------')
k=1
while(k<3):
    print(k)
    k+=1

# loop2:for
print('----------loop2----------')
s='done'
for c in s:
    print(c)

# loop3:for+range
print('----------loop3----------')
for n in range(0,4):
    print(n)

# loop4:for+列表解析,数据量较少时使用
print('----------loop4----------')
for j in [i+1 for i in range(10) if i % 2 ==0]:
    print(j)

# 把字符转换为数值
print('----------把字符转换为数值 ----------')
numA=Decimal('3')
print(numA**2)
