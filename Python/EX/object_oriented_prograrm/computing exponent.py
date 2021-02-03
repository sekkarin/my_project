#เวียนวายตายเกิด
#computing exponent

def exp(x,n):
    if n ==0:
        return 1
    else:
        return x*exp(x,n-1)

print("Exponet of 2 ** 4 = ",exp(2,4))

def factorial(n):
    if n == 1:
        return 1
    else:
        res = n*factorial(n-1)
        return res
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#call both function
print("factorial (4) = ",factorial(5))
print("factorial (5) =",fib(5))