#calculating factorial of a number using function
#Here I use recursive function.
def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        return n* factorial(n-1)

a = int(input("Enter the number: "))
#calling the function
result = factorial(a)
print("Factorial of",a,"is:",result)
