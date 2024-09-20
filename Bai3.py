import numpy
a=int(input())
b=int(input())

arr=numpy.random.rand((b-a))*(b-a)+a
print(arr)