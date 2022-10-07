#结合本周理论课所学内容，使用三种方法求根号2的近似值：牛顿-拉弗森法
def newton_raphson(k, e):
    guess = k
    while abs(guess * guess - k) >= e:
        guess = guess - (((guess * guess) - k) / (guess * 2))
    return guess


print(newton_raphson(2, 0.00000000001))