#simpler cal +,-,*,/
def add(a,b):
    answer = a + b 
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def tyms(a,b):
    answer = (a*b)
    print(str(a) + "*" + str(b) + "=" + str(answer))
    

print("A. Addition")
print("B. Substraction")
print("C. division")
print("D. Multiplication")
print("Q. Quit")

choice = input("Enter your choice: ")

if choice == "A":
    print("Addition")
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    add(a, b)

elif choice == "B":
    print("subtraction")
    a = int(input("Enter your first num: "))
    b = int(input("Enter your second number:"))
    sub(a,b)

elif choice == "C":
    print("division")
    a = int(input("Enter your first num: "))
    b = int(input("Enter your second number:"))
    div(a,b)

elif choice == "D":
    print("Multiply")
    a = int(input("Enter your first num: "))
    b = int(input("Enter your second number:"))
    tyms(a,b)

elif choice == "Q":
    print("Quit")
    quit()





 

 


