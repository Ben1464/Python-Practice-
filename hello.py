def hello():
    print("Hello World")
hello()

list_courses= ["SE","DS", "DevOPS"]
print("list_courses",list_courses)
print(list_courses[2])

name = "Ben"
age =28
course = "Software enginerring"
school = "Moringa school"
print(f"My name is {name} i am {age} old and i am currently learing {course} at {school}")

price_1=250
price_2=400
print(f"The shirt cost Ksh {price_1} and the lunch consted us Ksh {price_2}")

def good_morning(name="Racheal"):
    print(f"Good morning {name}")
    good_morning()
    
    
#Example of a sequence 
my_list =[1,2,3,4,5]
print (my_list[2])
print (my_list[3])
#Example of a tuple
my_tuple = (3,79,"Alex",6.2,"James")
print(my_tuple[3])
print(my_tuple[0:3])
#Sequence operations
s = [3,5,9,0,12,17.3]
17.3 in s #This will return "true"
#Python list and its methonds 
marks = [23,56,87,90,45]
marks.sort()
print(marks)

my_list = [2,1,7,9,4,0,23]
my_list.sort(reverse=True)
print(my_list)

#Sorting strings by their aphabetical order 
my_list = ["Cabbage","Aples","Spinach","Melons","Oranges"]
my_list.sort()
print(my_list)
#Sorting by length
my_list.sort(key=len)
print(my_list)

students = ["Antony","Alexander","Ben","Kamau"]
students.sort()
print(students)

students = ["Antony","Alexander","Ben","Kamau"]
students.sort(reverse= True)
print(students)

#Sorting using key value 
my_list = [('John', 1), ('Steve', 2), ('Joe', 3)]

# We can define a function for the list to sort by the second key

def sort_tuple(tuple_value):

    # return the key we want to sort by
    return tuple_value[1]

my_list.sort(key = sort_tuple)
print(my_list)
#Adding elements to an exisiting list .append ()(only add the element at the end of the list)
my_list = [12,11,15,28,29]
my_list.append(10)
print (my_list)
#Adding elements using .insert()
my_list = [3,5,8,4]
my_list.insert(4,7)
print (my_list)

my_list = ["a", "b", "c", "d", "e", "f"]
my_list.insert(6,"g")
print (my_list)
my_list.insert(3, "c")
print (my_list)

#Removing and element from a list
# del()
my_list = ["a","b","c","d","e","f","g","h","i","j"]
del(my_list[2])
print(my_list)
#list.pop()(if used without index it remeoves the last element of the list)
fruits = ["Mangos","Apple","Oranges","Melons"]
fruits.pop(2)
print(fruits)
#list.remove () (Searches by value instead of by index)
courses = ["Devops","SE","Cyber Security","Data Science"]
courses.remove ("Devops")
print(courses)
#list.clear () (clears all the values of the list)
products =["Absolute","Integra","Optimizer","Ranger"]
products.clear()
print (products)
#Range(range is used in a for loop and can only contain integers)
my_range = range (6)
print(my_range)

my_range = range (2,10,2)
print (my_range)
#strings(strings are iterable, they can be looped through)
greatings = "Hello everyone"
for letters in greatings:
    print (letters)

#one can change the format of a string using the following methods, str.uppercase (),str.lowercase ().  

 #Python dictionaries are built in data types that store key-value pairs it allow users to associate values (value) with unique identifiers (keys)
    my_dict = {"name":"Ben","age":28,"course":"SE"} 
    print(my_dict["age"])    
    print(my_dict["course"])
    print(my_dict["name"])
    print(my_dict)
    
    
 #Algorithims basics
    #algorithms are step by step or formula of solving a specific problem
    #In python they are implemeneted using functions,loops and conditional statemensts 
    # variables and data types
    x=5
    y=6
    z=x+y
    print(z)   

    #While declaring variables, variables can be declared withh more than one values
    x,y,z = "Bananas","Apples","Oranges"
    print(x)
    print(y)
    print(z)

    #Conditional statements 
    age = 38
    name = "Alex"
    if age <= 18:
        print(f"{name} is under age")
    else:
        print(f"{name} is an adult" )

    price = 1250
    product_1 = "Sugar"   
    product_2 = "Coffee"
    if price >= 500:
        print(f" you can buy {product_1}")
    else:
        print(f"Save the money sugar isnt that neccesary or you can buy {product_2}")

   #Loops (for,while) 
        #for loop    
    for i in  range(10):
        print(i)

    #while loop
    i = 10
    while i <= 10:
        print(i)
        i+=1

    count = 0
    while count < 5:
        print(count)
        count += 1

#A fuction that add elements to a list using .append method
     
def add_six_to_list(my_list):
        my_list.append(6)
        return my_list
original_list = [1,2,3]
new_list = add_six_to_list(original_list)
print(new_list)

#Converting a string to a list using .split()

Greatings = "Good morning gentlemen"
print(Greatings.split())

#Converting a list to a string using .join()

my_list = ["Good","morning","gente"]
print(" ".join(my_list))

#Assiging one variable to more than one value

x=y=z = "Alphabets"
print(x)
print(y)
print(z)

#Global variables declaration (variables created outside a function)
x="Awesome!"
def fun():
    print("Python is" + x)
    
fun()

#Object oriented programing (using objects)

class Dog:
    pass
fido = Dog() #New instance 
fido
snoppy = Dog() #New insrance 
snoppy
tommy = Dog()#New instance 
tommy

