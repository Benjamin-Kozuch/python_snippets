


'''
Flatten a list of lists using a generator
'''

my_list = [1, [2, 3], 4, [5, [6, 7], 8]]

def flatten_list_of_lists(my_list):
    for element in my_list:
        if isinstance(element, list):
            yield from flatten_list_of_lists(element)
        else:
            yield element

for i in flatten_list_of_lists(my_list):
    print(i)



#The following code also works without using 'yield from'

# def flatten_list_of_lists_v2(my_list):
#     for element in my_list:
#         if isinstance(element, list):
#             for sub_element in flatten_list_of_lists_v2(element):
#                 yield sub_element
#         else:
#             yield element

# l = []
# for element in flatten_list_of_lists_v2(my_list):
#     print(element)


