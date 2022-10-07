#遍历练习：写⼀个Python程序，输出1-100中所有奇数，并求这些50以内奇数的乘积。
C = 1
for i in range(1,100):
    if i%2==1:
        print(i)
        if i<= 50:
            C*=i
print(C)