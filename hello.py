def hello():
    print("Hello world!")

hello()

list_courses= ["SE","DS", "DevOPS"]
print("list_courses", list_courses)

name = "Ben"
age =28
course = "Software enginerring"
school = "Moringa school"
print(f"My name is {name} i am {age} old and i am currently learing {course} at {school}")

price_1=250
price_2=400
print(f"The shirt cost Ksh {price_1} and the lunch consted us Ksh {price_2}")

def good_morning(name="Enginers"):
    print(f"Good morning {name}")
    good_morning()
    good_morning("Ben")

def stylish_painter ():
    best_hairstyle = "kinky"
    return "Micheal Jackson"
stylish_painter()
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
my_list = [2,1,7,9,4,0,23]
my_list.sort()
print(my_list)

#Sorting strings by their aphabetical order 
my_list = ["Cabbage","Aples","Spinach","Melons","Oranges"]
my_list.sort()
print(my_list)
#Sorting by length
my_list.sort(key=len)
print(my_list)
#Sorting using key value 
my_list = [('John', 1), ('Steve', 2), ('Joe', 3)]

# We can define a function for the list to sort by the second key

def sort_tuple(tuple_value):

    # return the key we want to sort by
    return tuple_value[1]

my_list.sort(key = sort_tuple)
print(my_list)

