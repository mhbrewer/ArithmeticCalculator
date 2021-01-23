from ExpressionFactory import ExpressionFactory

class RawExpression:
  expressionString = ""

  def isValid(self):
    if not self.isRightParenOrNumeric(self.expressionString[-1]):
      return False
    if not self.isLeftParenOrNumeric(self.expressionString[0]):
      return False
    return True
  
  def isLeftParenOrNumeric(self, char):
    return char == "(" or char.isnumeric()
  
  def isRightParenOrNumeric(self, char):
    return char == ")" or char.isnumeric()

  def __init__(self, inputExpression):
    self.expressionString = inputExpression