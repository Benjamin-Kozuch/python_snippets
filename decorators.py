'''
level I
Define a function that defines a second function and returns that second function
and within that second function CALL the function that was passed into the first defined function
(and return the value the CALLing that function returns)

level II
if the function you are decorating takes parameters,
pass in *args, **kargs into the second function and 
pass in *args, **kargs into the function CALL thats within the second function

level III
If you want to pass a paramter into the decorator itself,
then define a function that has everything that we mentioned above 
and returns the outermethod




'''

# level I  ####################################################################
import time

def record_time_elapsed(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(str(end - start))
        return result
    return wrapper

@record_time_elapsed
def ad():
    time.sleep(2)
    print(str(1+1))

'''Is equivalent to writing:'''
#ad = record_time_elapsed(ad)

#print(ad.__name__) #  in level IV well see how to maintain the original name

#ad()









# level II ####################################################################

def record_time(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result =  func(*args, **kargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper



@record_time
def add2(a,b):
    time.sleep(1.5)
    print(str(a+b))

#add2(4,6)


# level III ####################################################################

#should only print time elapsed if the time elapsed is more than 5 seconds.

def record_time_takes(more_than_5=False):
    def second_wrapper(func):
        def wrapper(*args, **kargs):
            start = time.time()
            result =  func(*args, **kargs)
            end = time.time()
            if more_than_5 and end-start > 5:
                print(end-start)
            elif not more_than_5:
                print(end-start)
            return  result
        return wrapper
    return second_wrapper




@record_time_takes(more_than_5=True)
def add3(a,b):
    time.sleep(4)
    print(str(a+b))

#add3(30,40)


# level IV ####################################################################

# Add @functools.wraps(func) as a wrapper to the inner most function

from functools import wraps

def record_the_time_elapsed(on=False):
    def outer_function(func):
        @wraps(func)
        def inner_function(*args, **kargs):
            print("in wrapper")
            result = func(*args, **kargs)
            print("in wrapper2")
            return result
        return inner_function
    return outer_function


@record_the_time_elapsed(on=False)
def add4(a,b):
    """Testing to see if add4.__doc__ shows up because we used @wraps"""
    print(str(a+b))

add4(30,40)
print(add4.__name__, add4.__doc__)