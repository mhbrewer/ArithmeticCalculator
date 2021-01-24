from ExpressionFactory import ExpressionFactory
from Validator import Validator

class RawExpression:
  expressionString = ""
  validChars = ["+", "*", "-", "/", "(", ")"]
  validator = Validator()

  def isValid(self):
    return self.validator.isValidExpression(self.expressionString)

  def evaluate(self):
    return 0

  def __init__(self, inputExpression):
    self.expressionString = inputExpression
