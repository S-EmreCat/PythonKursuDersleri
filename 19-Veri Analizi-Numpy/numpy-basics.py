
import numpy as np

# python-list
py_list=[1,2,3,4,5,6,7,8,9]


# numpy array
                     # (1,2,3,4) yaparsak her sayıyı farklı bir parametre olarak alır

np_array=np.array([1,2,3,4,5,6,7,8,9])  # diziyi tek bir parametre olarak göndermek için bu şekilde yapıyoruz

# print(type(np_array)) >> <class 'numpy.ndarray'>

py_multi_list=[[1,2,3],[4,5,6],[7,8,9]]

np_multi_array=np_array.reshape(3,3)

print(py_multi_list)
print(np_multi_array)

# print(len(np_array)) >> 9
# print(np_array.ndim) >> 1