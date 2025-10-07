print("--------------Simple Calculator---------------------")
a=int(input("enter number:"))
b=int(input("enter number:"))
operator=input("enter operators(+,-,*,/,%)")
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
elif operator=='%':
    print(a%b)
else:
    print("Invalid")
        