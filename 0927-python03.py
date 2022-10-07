#字符串练习：写一个Python程序，
# 判断一个输⼊的字符串s，
# 是否包含两个或两个以上连续出现的相同字符组成的字符串，
# 并输出最长连续出现的字符长度。
str= input("请输入字符串:\n")
i = 1
curMaxLen = 1
maxLen = 1
r = 0
while i < len(str):
    if str[i] == str[i -1]:
        r = 1
        i += 1
        curMaxLen += 1
    else:
        i += 1
        curMaxLen = 1
    if curMaxLen > maxLen:
        maxLen = curMaxLen
if r == 1:
    print("Find!")
    print(maxLen)
else:
    print("No exist!")
