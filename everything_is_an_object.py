
name = "Enki"
age = 26
age_float = 26.0
user_dict = {"name":name, "age":age}
user_list = [name, age]
user_tuple = (name, age)

# Every piece of data in Python is an object. And all objects in python are instantiated of a class.
# Classes are blueprints that describe what an object should look like.
# There is a builtin class for every data type. So when you use a certain data type in your program
# python instantiates the class of that type to give back an object representation of that data.
# Thats how you can use the various builtin methods and attributes for that data type.
print(type(name), type(age), type(age_float), type(user_dict), type(user_list), type(user_tuple))
