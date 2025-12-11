import numpy as np
#array attributes and shapes:
data = np.array([1,2,3,4,5,6])
print(data)

#reshape of array:
data1 = np.arange(1,13)
new_arr = np.reshape(data1,(3,4))
print(new_arr)

#convert 2d array into 1d array:
#1.flatten():
data = np.array([20,20,40,50,60])
x = data.flatten()
x[0] = 90
print(data)
print(x)

#2.ravel()
data = np.array([20,20,40,50,60])
x = data.ravel()
x[0] = 90
print(data)
print(x)

#3.view()
data = np.array([20,20,40,50,60])
x = data.view()
x[0] = 90
print(data)
print(x)

#4.copy()
data = np.array([20,20,40,50,60])
x = data.copy()
x[0] = 90
print(data)
print(x)

#Airthmetic operators:
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,0,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Mathemetical operations:
arr = np.array([1,4,7,16,24])
arr_1 = np.min(arr)
print(arr_1)
arr_2 = np.max(arr)
print(arr_2)
arr_3 = np.mean(arr)
print(arr_3)
arr_4 = np.median(arr)
print(arr_4)
arr_5 = np.var(arr)
print(arr_5)
arr_6 = np.std(arr)
print(arr_6)
arr_7 = np.sqrt(arr)
print(arr_7)
arr_8 = np.exp(arr)
print(arr_8)
arr_9 = np.log(arr)
print(arr_9)
arr_10 = np.sin(arr)
print(arr_10)
arr_11 = np.cos(arr)
print(arr_11)

#Q. create a array 1 to 16 with 4*4 pattern and then convert it into 1d aaray
arr = np.arange(1,17)
new_arr = np.reshape(arr,(4,4))
print(new_arr.flatten())
print(arr.size)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.var(arr))


#Q. Perform opertions of square,subtraction by 10,minimum,mean, maximum, mean, median
arr = np.array([[10,20,30],[40,50,60]])
print(arr)
arr_1 = np.square(arr)
print(arr_1)
arr_2 = (arr-10)
print(arr_2)
arr_3 = np.min(arr)
print(arr_3)
arr_4 = np.max(arr)
print(arr_4)
arr_5 = np.mean(arr)
print(arr_5)
arr_6 = np.median(arr)
print(arr_6)

#Q. 
array = np.linspace(1,501,100)
print(array)
arr_1 = np.min(array)
print(arr_1)
arr_2 = np.max(array)
print(arr_2)
arr_3 = np.mean(array)
print(arr_3)
arr_4 = np.median(array)
print(arr_4)
arr_5 = np.std(array)
print(arr_5)
arr_6 = np.var(array)
print(arr_6)
array_2 = np.reshape(array,(10,10))
print(array_2)








