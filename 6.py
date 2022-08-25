# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

num=int(input("Enter 1st number:"))

while(num>=10):
    num=num%10
print("The first digit of numher",+num)