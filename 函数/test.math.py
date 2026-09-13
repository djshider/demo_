# test_math.py
import my_math

# 1. 调用模块函数
print("10 + 5 =", my_math.add(10, 5))
print("10 - 5 =", my_math.subtract(10, 5))
print("10 * 5 =", my_math.multiply(10, 5))

# 2. 使用模块变量 pi 计算圆面积（半径 r=3）
r = 3
area = my_math.multiply(my_math.pi, my_math.multiply(r, r))
print("半径3的圆面积 =", area)