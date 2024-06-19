# PROGRAM OF CALCULATOR

print("***~~~~~~~MINI CALCULATOR~~~~~~~~~***")
num1=float(input("enter first number"))
num2=float(input("enter the second number")) 
print("Press 1 for Addition \n Press 2 for subtraction \n press 3 for multiplication \n Press 4 for division ")
choice=int(input("Enter your choice form 1-4 : "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("Invalid Choice")