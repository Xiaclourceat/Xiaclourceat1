#蒙特卡罗求积分
# 根据蒙特卡罗思想，⽤Python编写程序计算区间[0,1]上定积分：
import random
import math
S = 1*2
N = 10000000
C = 0
for i in range(N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,2.0)
    if y <= math.pow(x,2) + math.pow(x,3):
        C += 1
I = C/N *S
print(I)