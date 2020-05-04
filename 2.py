#	Accept n number from user and calculate the sum of all number between 1 and n including n
num = int(input("Enter the value of n: "))
new = num
sum= 0
#checking for positive no
if num <= 0:
   print("Please enter a positive number")
else:
   while num > 0:
        sum = sum + num
        num = num - 1;

print("Sum of n natural numbers is: ", sum)
