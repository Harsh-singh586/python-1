a = int(input("Enter first number "))
b = int(input("Enter second number "))
c  = int(input("Enter 1 for addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n"))
if c ==1:
    print("Output is "+str(a+b))
elif c==2:
    print("Output is "+str(a-b))
elif c==3:
    print("Output is "+str(a*b))
elif c==4 and b!=0:
    print("Output is "+str(a/b))
elif c==4 and b==0:
    print("Second number cannot be 0")
else:
    print("Wrong Operator choosen")
