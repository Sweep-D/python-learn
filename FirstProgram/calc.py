'''
    Program: The god damn best calculator ever
    Author: Sweep
    Copyright: ?
'''
# Actual first program. Making a calculator
import re

print("The god damn best calculator ever")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""

    # If there has been a previous calculation, use that result as the prompt
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # if user quits ->
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[A-Za-z,:;.()" "]', '', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)


while run:
    performMath()
