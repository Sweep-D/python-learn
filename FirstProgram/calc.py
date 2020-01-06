# Actual first program. Making a calculator
import re

print("The god damn best calculator ever")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[A-Za-z,:;.()+" "]', '', equation)
        previous = eval(equation)
        print("You typed:", previous)


while run:
    performMath()