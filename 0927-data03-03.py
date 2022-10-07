#拉马努金公式

def factorial(n):
    if  n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))

x = 0
x+=2*pow(2,0.5)/9801*factorial(4*0)*(1103+26390*0)/pow(factorial(0),4)/pow(396,4*0)
i = 1
while abs(1/x-3.1415926535)>0.0000000001:
    x+=2*pow(2,0.5)/9801*factorial(4*i)*(1103+26390*i)/pow(factorial(i),4)/pow(396,4*i)
    i+= 1
print(1/x)
print("迭代次数为:")
print(i)