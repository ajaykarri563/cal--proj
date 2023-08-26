import math
import parser as pr

def add(a, b):
    return a + b
def red(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def power(a, b):
    return a ** b

def statement_wrapper():
    doper = {
         '+' : add
        ,'-' : red
        ,'*' : mul
        ,'/' : div
        ,'^' : power
    }
    states=raw_input(">>")
    result=pr.apply(states, darg=doper)
    if(result == None):
        print("<< Undefined")
    else:
        full = "<< ", str(result)
        print(full)
    return

while True:
    print("\n CALCULATOR MENU")
    print("1  Addition:      ")
    print("2  Subtraction:   ")
    print('3  Multiplication:')
    print("4  Raise to power:")
    print("5  Division:      ") 
    print("6  Floor division:")
    print("7  Factorial:     ")
    print("8  Statement based:")
    choice=int(input("enter any choice:"))
    def additon():
        a=int(input("enter 1st no to perform addition:"))         
        b=int(input("enter 2nd no to perform addition:"))          
        c=add(a, b)
        print("sum is:",c)
        
    def subtract():
        a = int(input("enter 1st no to perform subtraction:"))
        b = int(input("enter 2nd no to perform subtraction:"))
        c = red(a, b)
        print("subtraction is:", c)

    def multiplication():
        a = int(input("enter 1st no to perform multipication:"))
        b = int(input("enter 2nd no to perform multiplication:"))
        c = mul(a, b)
        print("multiplication is:", c)
        
    def power():
        a = int(input("enter base :"))
        b = int(input("enter power :"))
        c = pow(a, b)
        print("division is:", c)
        

    def divide():
        a = int(input("enter 1st no to perform division:"))
        b = int(input("enter 2nd no to perform division:"))
        c = div(a, b)
        print("division is:", c)
        
    def floor_division():
	    a = int(input("enter 1st no to perform floor division:"))
	    b = int(input("enter 2nd no to perform floor division:"))
	    c = a // b
	    print("floor division is:",c)
        
    def factorial():
        res = 0
        num = int(input("enter a number: "))
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            res = math.factorial(num-1)*num
            print("The factorial of",num,"is:",res)
        

    if choice==1:
        additon()
    elif choice==2:
        subtract()
    elif choice==3:
        multiplication()
    elif choice==4:
        power()
    elif choice==5:
        divide()
    elif choice==6:
        floor_division()
    elif choice==7:
        factorial()
        #break
    elif choice==8:
        statement_wrapper()
    else:
        print("wrong input")
        exit(0)

