from ExpressionFactory import ExpressionFactory
from Validator import Validator

class RawExpression:
  fullExpression = ""
  validator = Validator()
  factory = ExpressionFactory()
  expressionHead = None

  def isValid(self):
    return self.validator.isValidExpression(self.fullExpression)

  def evaluate(self):
    if self.isValid() and (self.expressionHead is None):
      self.buildExpressionTree()
    return self.expressionHead.evaluate()
  
  def buildExpressionTree(self):
    self.expressionHead = self.__buildExpressionTree(self.fullExpression)
  
  def __buildExpressionTree(self, expressionInput):
    if len(expressionInput) == 1:
      return self.factory.CreateExpression(expressionInput)
    else:
      breakPoint = self.findValidBreakpoint(expressionInput)
      return self.factory.CreateExpression(
        self.__buildExpressionTree(expressionInput[:breakPoint]), 
        expressionInput[breakPoint], 
        self.__buildExpressionTree(expressionInput[breakPoint+1:]))

  def findValidBreakpoint(self, expressionInput):
    for i in range(len(expressionInput)):
      if expressionInput[i] == "+" or expressionInput[i] == "-":
        return i
    return 1

  def __init__(self, inputExpression):
    self.fullExpression = inputExpression


