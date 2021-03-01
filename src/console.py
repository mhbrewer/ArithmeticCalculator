from RawExpression import RawExpression

#!/usr/bin/env python
haveValidEquation = False
while(not haveValidEquation):
  print("Please enter an equation.")
  print("x = ")
  inputString = input()
  expression = RawExpression(inputString)
  if expression.isValid():
    haveValidEquation = True
  else:
    print("Invalid Equation.")

print("x = " + str(expression.evaluate()))


