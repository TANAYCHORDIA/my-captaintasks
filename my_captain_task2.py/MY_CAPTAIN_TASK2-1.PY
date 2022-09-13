#This code is used for finding the Fibonacci number of the nth term 
def Fibonacci(n):
    if n<0:
        print("Invalid input")
    elif n==1 or n==2:
        return 1
    elif n==0:
        return 0
    else:
        return Fibonacci (n-1)+Fibonacci(n-2)
n=int(input("enter a fibonacci term:"))
print(Fibonacci(n))


