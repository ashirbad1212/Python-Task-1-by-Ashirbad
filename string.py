#Accept string from a user and display only those characters which are present at an even index number.
def EvenIndexChar(str):
  for i in range(0, len(str)-1, 2): #i increaes by 2 so as to print even index
    print("index[",i,"]", str[i] )
Str = input("Enter String ")
print("Orginal String is ", Str)
print("Printing only even index characters")
EvenIndexChar(Str)