import numpy
result_array = numpy.empty((0))

for i in range(10):
    result_array = numpy.append(result_array, [i])
print("result is :")
print(result_array)
