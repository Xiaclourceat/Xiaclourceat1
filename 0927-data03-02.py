pi = 0
i = 0
while abs(pi-3.1415926535)>0.0000000001:
    pi+=16*pow(-1,i)*(1/((2*i+1)*pow(5,(2*i+1))))-4*pow(-1,i)*(1/((2*i+1)*pow(239,(2*i+1))))
    i+= 1
print(pi)
print("迭代次数为:")
print(i)