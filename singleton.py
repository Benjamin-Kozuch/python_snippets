'''

Here is an example of how to create a singleton class,
The idea is that we have a class variable called _instance initialized to None
Every time we try to create an instance of this class, __new__ is called to create that instance.
Once __new__ creates the instance, that instance is passed to the __init__ methos to intialize that instance with certain values etc.

In the __new__ method, we will create a new instance 
and set out _instance variable to equal to that instance,
if and only if that _instance variable is equal to None 
(i.e. an instance hasnt yet been created, or it has been created but has since been deleted)

If an instance HAS previously been created and _instance is already set to that instance,
we can so a couple things:
1) return None
2) return the previously created instance
3) raise an exception


'''



class Server:
    _instance = None

    def __new__(cls):
        print('new called', str(cls))
        if not cls._instance:
            cls._instance = super(Server, cls).__new__(cls)
            # or this --> cls._instance = object.__new__(cls, *args, **kargs)
        else:
            return
        return cls._instance

    def __init__(self, number):
        print('init called with: ', str(number))

    
    def __del__(self):
        print('delete called')



s1 = Server(5)
# print(s1._instance)
# s2 = Server()

# print(s1)
# print(s2)