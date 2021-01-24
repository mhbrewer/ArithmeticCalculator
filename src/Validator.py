

class Validator:
  validChars = ["+", "*", "-", "/", "(", ")"]
  
  def isValidExpression(self, expression):
    if expression == "":
      return False
    return ( 
      self.hasCorrectEnds(expression) 
      and self.hasValidChars(expression) 
      and self.hasValidParens(expression) 
      and self.hasValidCharArrangement(expression) 
      )

  def hasValidCharArrangement(self, expression):
    lastCharWasNumOrRParen = True
    for char in expression:
      if not lastCharWasNumOrRParen and char in self.validChars:
        if not char == "(":
          return False
      lastCharWasNumOrRParen = char.isnumeric() or char == ")"
    return True

  def hasValidParens(self, expression):
    OpenParenthesis = 0
    for char in expression:
      if char == "(":
        OpenParenthesis += 1
      if char == ")":
        OpenParenthesis -= 1
      if OpenParenthesis < 0:
        return False
    return OpenParenthesis == 0
  
  def hasValidChars(self, expression):
    for char in expression:
        if not (char in self.validChars or char.isnumeric()):
          return False
    return True

  def hasCorrectEnds(self, expression):
    return (self.isRightParenOrNumeric(expression[-1])
      and self.isLeftParenOrNumeric(expression[0]))

  def isLeftParenOrNumeric(self, char):
    return char == "(" or char.isnumeric()
  
  def isRightParenOrNumeric(self, char):
    return char == ")" or char.isnumeric()

  def __init__(self):
    pass