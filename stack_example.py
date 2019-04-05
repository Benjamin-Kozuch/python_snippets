'''

// Given a string representing a postfix expression e.g. 5 3 + 2 -
// write a function that evaluates this expression.
//
// Examples: "3 4 +" = 7
//           "4 2 + 4 1 - /" = 2
//           "1 2 3 4 5 + + + +" = 15

'''

'''

1) reached operator and last two things on the list are not numbers
2) reached operator and theres only one thing left on the list
3) reached the end and theres more than 1 numbers left

'''




def calc(a, b, operation):
    
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b

def stack_pop(stack):
    
    if len(stack) == 0:
        raise ValueError()
    



def post_fix(expression):
    
    stack = []
    
    characters = expression.split(" ")
    
    for character in characters:
        if character in "+-/*":
            
            
            
            
            second_character = int(stack.pop())
            first_character = int(stack.pop())
            
            
            
            
            result = calc(first_character, second_character, character)
            stack.append(str(result))
        else:
            stack.append(character)
            

    return stack.pop()
            
        
    
    




answer = post_fix("3 4 +")
print(answer)

answer = post_fix("4 2 + 4 1 - /")
print(answer)

answer = post_fix("1 2 3 4 5 + + + +")
print(answer)




print(stack_pop([]))

