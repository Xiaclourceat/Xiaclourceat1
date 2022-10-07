#结合本周理论课所学内容，使用三种方法求根号2的近似值：逐步逼近法
def f():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
    while abs(g*g-c)>0.01:
        g+=0.00001
        i=i+1
        print("%d:g=%.5f"%(i,g))

f()