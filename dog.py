# this is for python3. when you create a class in python2.7 you use the object keyword.
# class ClassName(object):

class Dog():
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age
        # any variable prefixed with self is available to every method in the class.
        # variables accessible through instances like this are called attributes


    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title()+ " is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title()+" rolled over!")


# __init__ is a special method python runs automatically. self is special and must come first.  every method call associated with a class must reference to the instance itself, which is what self does?
# it gives the individual instance access to the attributes and methods in the class.
# so if we made an instance of dog, python will call the __init__ method, we don't need to pass self (it is done automatically) and we would pass name and age
