import numpy

A = numpy.array([1,2,3,4],[5,6,7,8])
B = numpy.repeat(A,2).reshape(A.shape[0], A.shape[1], -1)
C = numpy.stack((A,A))
print(A)
print(B)
print(C)