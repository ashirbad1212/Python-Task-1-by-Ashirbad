#Write a python program to print the Fibonacci series and also check if a given input number is Fibonacci number or notdef Fibonacci(num):
c=int(input("Enter the no of terms"))
t1=0
t2=1
i=0
while i<c:
    print(t1)
    s=t1+t2
    t1=t2
    t2=s
    i=i+1
num=int(input("Enter your no to check whether it is fibonacci or not"))
import math
def fib(n):
  k=int(math.sqrt(n))
  if pow(k,2)==n:
      return True
  else :
      return False
def fibo(n):
      r1=5*n*n+4
      r2=5*n*n-4
      if fib(r1) or fib(r2):
          return True
      else:
          return False
if fibo(num):
    print("it is a fibonacci no")
else:
    print("no it is not a fibonacci no")

