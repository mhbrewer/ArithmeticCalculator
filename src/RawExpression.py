from ExpressionFactory import ExpressionFactory

class RawExpression:
  expressionString = ""
  validChars = ["+", "*", "-", "/", "(", ")"]

  def isValid(self):
    if self.expressionString == "":
      return False
    return ( self.hasCorrectEnds() and self.hasValidChars() 
      and self.hasValidParens() and self.hasValidCharArrangement() )
  
  def hasValidCharArrangement(self):
    lastCharWasNumOrRParen = True
    for char in self.expressionString:
      if not lastCharWasNumOrRParen and char in self.validChars:
        if not char == "(":
          return False
      lastCharWasNumOrRParen = char.isnumeric() or char == ")"
    return True

  def hasValidParens(self):
    OpenParenthesis = 0
    for char in self.expressionString:
      if char == "(":
        OpenParenthesis += 1
      if char == ")":
        OpenParenthesis -= 1
      if OpenParenthesis < 0:
        return False
    return OpenParenthesis == 0
  
  def hasValidChars(self):
    for char in self.expressionString:
        if not (char in self.validChars or char.isnumeric()):
          return False
    return True

  def hasCorrectEnds(self):
    return (self.isRightParenOrNumeric(self.expressionString[-1])
      and self.isLeftParenOrNumeric(self.expressionString[0]))

  def isLeftParenOrNumeric(self, char):
    return char == "(" or char.isnumeric()
  
  def isRightParenOrNumeric(self, char):
    return char == ")" or char.isnumeric()

  def __init__(self, inputExpression):
    self.expressionString = inputExpression
    