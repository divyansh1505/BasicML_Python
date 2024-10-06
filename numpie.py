import numpy as np 

arr = np.array([1, 2, 3])
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)  # Output: [5 7 9]

zeros = np.zeros((2, 3))  # 2x3 array of zeros
randoms = np.random.rand(3, 3)  # 3x3 array of random numbers

print(zeros)
print(randoms)

arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))  # Output: Mean of the array
print(np.std(arr))   # Output: Standard deviation

temps_celsius = np.array([0, 10, 20, 30])

temps_fahrenheit = temps_celsius * 9/5 + 32

print(temps_fahrenheit)
