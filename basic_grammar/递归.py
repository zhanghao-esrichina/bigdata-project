
# 递归的次数是入口决定的，防止死循环的关键在于是否规划好“何时退出循环”

print("\n")
print("demo1")


def sum(x):
    if x == 0:
        return 0
    else:
        return x+sum(x-1)


print(sum(10))


print("\n")
print("demo2")


def sum1(n):
    if n > 100:
        return 0
    else:
        return n + sum1(n+1)

print(sum1(1))
