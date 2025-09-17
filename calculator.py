
# games of
def add(a,b):
    return a+b
def subtractor (a,b):
    return a-b
def multiply  (a,b):
    return a*b
def divide(a,b):
    if b==0:
        return("cannot divide by zero")
    return a/b



while True:
    print("1.add")
    print("2.subtractor")
    print("3.multiply")
    print("4.divide")
    print("5.exit ")

    choice = input ("enter choice (1-5):")

    if choice =="5":
     print("exiting------goodbye !")
     break


    num1=float(input("enter the first number :"))
    
    num2=float(input("enter the second number :"))

    if choice =="1":
        print ("result=", add(num1,num2))
 
    elif choice =="2":
        print("result=",subtractor(num1,num2))

    elif choice =="3":
        print("result=",multiply(num1,num2))  

    elif choice =="4":
        print("result=",divide(num1,num2))  

    else:
        print ("invalid choice ! try again .")        
