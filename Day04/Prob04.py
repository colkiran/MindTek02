
def fibo(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)

iter = int(input("Enter the number of iterations :"))
for i in range(iter):
    print(fibo(i), end=" ")

