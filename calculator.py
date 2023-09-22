print(" ".rjust(20),"Welcome to Apna Calculator")
print("Enter = for to see the output.")
a=int(input("Enter the number:"))
while True:
    n=input("Enter the operation:")
    if(n=='='):
        print("The answer is",a)
        break
    b=int(input("Enter the next number:"))
    if(n=='+'):a=a+b
    elif(n=='-'):a=a-b
    elif(n=='*'):a=a*b
    elif(n=='/'): a=a/b
    elif(n=='%'):a=a%b
    else:print("You press the wrong key.")
