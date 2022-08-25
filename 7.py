# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.

num=int(input("Enter 1st number:"))

while(num>=10):
    num=num//100
    num=num%10
print("The midile digit of numher",+num)



