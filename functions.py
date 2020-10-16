'''
def greet(name):
    print("hello" , name)
    print("Whats going on?")
greet("Paul")
print("This is outside greet()")


def add_two_numbers(num1 ,num2):
    answer = num1 + num2
    return answer
    #accepting my input
first_number = int(input("Enter first number"))
second_number = int(input("Enter second number"))
    #calling a function
solution = add_two_numbers(first_number,second_number)
    #displaying solution
print(first_number, "+" , second_number, "=" , solution)

#prnting the youngest child
def my_function(*kids):
    print("The youngest child is " + kids[2]) 
my_function("Emil" , "Tobias" , "Linus")
 

def my_function(child3 , child2 , child1):
    print("The youngest child is " + child3) 
my_function(child1 = "Emil" , child2 = "Tobias" , child3 = "Linus")   


#passing a listas an argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple" , "banana" , "cherry"]
my_function(fruits)       
'''
#exercise1
def distance_from_zero(num):
    num = float(input("Enter a number"))
    
    return num
distance_from_zero(-5.6)