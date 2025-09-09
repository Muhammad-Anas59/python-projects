print("Creating a simple calculator program : ")
print("Write quit to leave : ")
while True:
    n1=input("Enter the number: ")
    if n1.lower()=="quit":
        break
    n2=input("Enter the number: ")
    if n2.lower()=="quit":
        break
    operator=input("Enter any operator +,-,*,/ : ")
    if operator=="+":
        result=float(n1)+float(n2)
    elif operator=="-":
        result=float(n1)-float(n2)
    elif operator=="*":
        result=float(n1)*float(n2)
    elif operator=="/":
        if n2==0:
            print("Error! Division by zero : ")
        else:
            result=float(n1)/float(n2)
    else:
        print("Invalid operator : ")
    print("Result is: ", result)
print("THE END")

