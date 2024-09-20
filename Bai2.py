import numpy
a=int(input())
b=int(input())
array,step=numpy.linspace(a,b , num=(b-a+1),endpoint=True, retstep=True,dtype=int)
print(array)
print(step)


# axis trong linspace dung trong mang 2 chieu
#import numpy as np

# Tạo mảng 2 chiều
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# # Tính tổng dọc theo trục 0 (tổng các cột)
# sum_axis_0 = np.sum(array_2d, axis=0)
# print(sum_axis_0)  # Output: [5 7 9]

# # Tính tổng dọc theo trục 1 (tổng các hàng)
# sum_axis_1 = np.sum(array_2d, axis=1)
# print(sum_axis_1)  # Output: [ 6 15]

# #