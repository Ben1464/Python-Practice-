#Functions 

def my_function():
    print("First function to write ")
my_function()

#Passing urguments to functions 
def personal_info(name,age,sex,occupation):
    print(f"my name is {name} i am {age} and i am {sex} working as a {occupation}")

personal_info("Mwangi",21,"male","engineer")
personal_info("Kimani",52,"male","doctor")


def students_details(name,course,school):
    print(f"{name} is doing {course} in {school}. ")

students_details ("Beatrice","Software Engineer","Moringa school")
students_details ("Mercy","DevOPs","Moringa school")

#Passing arbitrary number of arguments
def my_family(*kids):
    print("The youngest child is "+ kids[3])
my_family("Mwangi","Kimani","Alex","Ben","James")    

#Returning values from functions
def my_function(name):
    return f"my name is {name}"
print(my_function("Mwangi"))
#strings concatenation in a function
def my_name (fname,lname,sirname):
    print(fname + ""+ lname +"" + sirname)
my_name("Alex","John","Mutwriri")    

#Passing a list as an urgumnet to a function 
def fruits_selection (fruits ):
    for x in fruits:
        print(x)
fruits = (["Apples","Bananas","Oranges"])
fruits_selection(fruits)

def programing_languages(languages):
    for x in languages:
        print (x)
languages = (["Java","JavaScript","Python",])
programing_languages(languages)

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
    
#Example of boolens
print(10<9)
print(10>9)
print(10==9)
print(10!=9)

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
    print(len(my_dict))

  #NB, the data types in a dictionary can be of any type 

    thisdict ={"brand":"mustang", "mileage": 20000,"year":1980,"color":["blue","red","black"]}
    print(thisdict)

    #To change an item in a dictionary
    thisdict["mileage"]= 30000
    print(thisdict)

    #To update the dictionary
    thisdict.update({"year":1990})
    print(thisdict)

    #Adding items to a dictionary
    thisdict["color"].append("yellow")
    print(thisdict)
    #One can also use the update method to add an item if the item is not there
    thisdict.update({"color":"Maroon"})
    print(thisdict)
    
    
 #Algorithims basics
    #algorithms are step by step or formula of solving a specific problem
    #In python they are implemeneted using functions,loops and conditional statemensts 
    # variables and data types
    x=5
    y=6
    z=x+y
    print(z)   

    #While declaring variables, variables can be declared with more than one values
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

    i =6 
    while i < 6:
        print (i)
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
#Convering a float to an integer
x=5.6
y=int(x)
print(y)
#convering a intenger to a float
x=5
y=float(x)
print(y)

#Example of boolens
print(10<9)
print(10>9)
print(10==9)
print(10!=9)

a= 300
b= 300
if a==b:
    print("True")
else:

    print("False")


c = 500
d = 300
if c>d:
    print("c is geater than d") 
else:
    print("d is greater than c")   

#More practice on while loops 
a=7
while a<10:
    print (a)   
    if a == 9:
        break
    a+=1

    #Classes 
    # The __init__() function is always executed when the class is being initiated
    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.age = 40 
print(p1.age)


class School:
    def __init__(self,name,location):
        self.name = name
        self.location = location

s1 = School("Moringa School","Nairobi")
print(s1.name)
print(s1.location)
s1.location = "Karen"
print(s1.location)

        
    
    #The __str__() function is used to return a string representation of the object
class Person:
        def __init__(self,name,age,sex):
            self.name = name
            self.age = age
            self.sex = sex
        def __str__(self):
            return f"{self.name} is {self.age} years old and he is {self.sex}"

p1 = Person("George", 26,"male")
print(p1)
p2 =Person("Mercy",19,"female")
print(p2)

class Course:
    def __init__(self,name,time,rate):
        self.name = name
        self.time = time
        self.rate = rate
    def __str__(self):
        return f"{self.name} costs {self.rate}"

c1 = Course("SE", 4, 200000)
print(c1)
c1.rate = 250000 #To change the rate from the initial declaration 
print(c1.rate)

#Object methods
#A method is a function that is defined inside the body of a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name + " and i am " + str(self.age) + " years old")

p1 = Person("Tonny", 16)
p1.myfunc()
#Python inheritance 
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
#The super () function is used to give access to the methods of a parent class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2018

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
print(x.graduationyear)
x.printname()
x.welcome()
#Iterators 
#Iterators are an object that can be iterated upon
#The __iter__() method is called once, and should return the iterator object itself

my_tuple = ("maize","rice","beans")
my_iter = iter(my_tuple)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

fruits = ["Apples","Bananas","Oranges"]
myit = iter(fruits)

print(next(myit))
print(next(myit))
print(next(myit))

#iteration in strings 
my_string = "Banana"
myit= iter(my_string)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping through an iterator
#To loop through an iterator, we can use a for loop
#The for loop actually creates an iterator object and executes the next() method for each loop

fruits_selection = ("apples","bananas","oranges")
for x in fruits_selection:
    print(x)

#Iterating through characters of a string 
    mystr = "hello"  
    for x in mystr:
        print(x)  

#Iteration that returns numbers 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))     

#Application of StopIteration
#StopIteration is raised when the next() method of an iterator has no further values

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 8:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
#lambda functions 
    #lambda functions are anonymous functions
    #A lambda function can take any number of arguments, but can only have one expression.

    x = lambda a: a+10
    print(x(5))

    x = lambda a,b : a*b
    print(x(3,9))

    x= lambda a,b,c : a+b*c
    print(x(3,4,5))

#Dates
    # The datetime module provides classes for manipulating dates and times

    import datetime
    x = datetime.datetime.now()
    print(x)

  # To return the date and the and the name of the week day
    
    import datetime
    x = datetime.datetime.now()
    print(x.strftime("%B %d, %Y"))

    import datetime
    x=datetime.datetime.now()
    print(x.strftime("%B %d, %Y %A . Today is victory of yourself yesterday,tommorrow is your victory of today."))  

    #local functions 

    def my_fun():
        x=300
        print(x)
    my_fun()

    #functions within a function

 
    def myfunc():
        x = 300
    def myinnerfunc():
        print(x)
        myinnerfunc()

myfunc()
  
  #Global scope
x = 700

def myfunc():
  print(x)

myfunc()

print(x)


#User input
firstname = input("Enter firstname: ")
print("Firstname: ", firstname)

lastname = input("Enter lastname: ")
print("Lastname: ", lastname)

email = input("Enter email:")
print("Email: ", email)

phone  = input("Enter phone")
print("Phone: ", phone)


    




