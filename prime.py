
lower = 500
upper = 600

print("the prime nos between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
num1= int(input("Enter a number: "))
if num1 > 1:
    # check for factors
    for i in range(2, num1):
        if (num1 % i) == 0:
            print(num1, "is not a prime number")
            break
    else:
        print(num1,"Is a prime no")
else:
    print(num, "is not a prime number")#since less than 1
