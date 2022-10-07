#结合本周理论课所学内容，使用三种方法求根号2的近似值：二分法
a=0
b=2
mid=1
while abs(mid**2-2)>=0.0000000001:
    if mid**2>=2:
        b=mid
    else:
        a=mid
    mid=(a+b)/2
print(mid)