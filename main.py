#Accept two integer numbers from a user and return their product and if the product is greater than 1000, then return their sum
def product_sum(num1, num2):
  product = num1 *num2
  if(product <= 1000):
    return product
  else:
    return num1 +num2

num1 = int(input("Please enter first number  "))
num2 = int(input("Now enter second number "))

result = product_sum(num1, num2)
print("The result is", result)
