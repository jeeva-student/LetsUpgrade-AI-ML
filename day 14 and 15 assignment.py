import numpy as np

print("question no:1\n")
dp = np.random.random((3, 3, 3,))
print(dp)

print("question no:2\n")
dp1 = np.diag([1,2,3,4])
print(dp1)

print("queston no:3\n")
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

print("question no:4\n")
x= np.random.random((3,3))
print("Original Array:\n")
print(x)
xmax, xmin = x.max(), x.min()
y = (x - xmin)/(xmax - xmin)
print("After normalization:\n")
print(y)

print("question no:5\n")
a = np.array([0, 1, 3, 4, 5, 6])
print("Array1: ",a)
b = [1, 4]
print("Array2: ",b)
print("Common values between two arrays:\n")
print(np.intersect1d(a, b))

print("question no:6\n")
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)

print("question no:7\n")
x = np.random.randint(0,2,6)
print("First array:\n")
print(x)
y = np.random.randint(0,2,6)
print("Second array:\n")
print(y)
print("Test above two arrays are equal or not!\n")
array_equal = np.allclose(x, y)
print(array_equal)

print("question no:8\n")
x = np.random.random(10)
print("Original array:\n")
print(x)
x[x.argmax()] = 0
print("Maximum value replaced by 0:\n")
print(x)

print("question no:9\n")
a = np.array([1, 2, 3, 4, 5])
print(a)

print("question no:10\n")
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)

print("question no:11\n")
Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)

print("question no:12\n")
A = np.random.randint(0,10,(3,3))
B= np.random.randint(0,10,(3,3))

x = np.diag(np.dot(A, B))
print(x)

print("question no:13\n")
Z = np.random.randint(0,10,50)
print (Z)
print('rank:', np.bincount(Z).argmax())

print("question no:14\n")
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5

print (Z[np.argsort(Z)[-n:]])

print("question no:15\n")
Z = np.array([("Hello", 2.5, 3),
              ("World", 3.6, 2)])
R = np.core.records.fromarrays(Z.T,names='col1, col2, col3',formats = 'S8, f8, i8')
print(R)