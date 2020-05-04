#	Given a number count the total number of digits in a number using python programming
n=int(input("Enter a  number:"))
count=0
while(n>0):
    count=count+1 #counting digits
    n=n//10  #extracting digit
print("The number of digits in the number are:",count)