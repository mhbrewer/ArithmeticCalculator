from ExpressionFactory import ExpressionFactory
from Validator import Validator

class RawExpression:
  fullExpression = ""
  validator = Validator()
  factory = ExpressionFactory()
  expressionHead = factory.CreateExpression(0)

  def isValid(self):
    return self.validator.isValidExpression(self.fullExpression)

  def evaluate(self):
    return self.expressionHead.evaluate()
  
  def buildExpressionTree(self):
    if len(self.fullExpression) == 1:
      self.expressionHead = self.factory.CreateExpression(self.fullExpression)
    else:
      self.expressionHead = self.factory.CreateExpression(
        self.factory.CreateExpression(self.fullExpression[0]), 
        self.fullExpression[1], 
        self.factory.CreateExpression(self.fullExpression[-1]))

  def __init__(self, inputExpression):
    self.fullExpression = inputExpression
    if self.isValid():
      self.buildExpressionTree()


