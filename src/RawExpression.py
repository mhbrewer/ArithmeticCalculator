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
    # print("****************************")
    # print("****************************")
    self.expressionHead = self.__buildExpressionTree(self.fullExpression)
  
  def __buildExpressionTree(self, expressionInput):
    # if len(expressionInput) == 0:
    #   print("Epmty Exp")
    #   return
    if len(expressionInput) == 1:
      return self.factory.CreateExpression(expressionInput)
    else:
      breakPoint = self.__findValidBreakpoint(expressionInput)
      # print(breakPoint)
      # print(expressionInput)
      if ((breakPoint+1 < len(expressionInput) and 
        (self.__rightExpressionIsParentheticalExcludeBreakPoint(expressionInput, breakPoint)
        or self.__rightExpressionIsParentheticalIncludeBreakPoint(expressionInput, breakPoint)) 
        and (breakPoint-1 >= 0 and self.__leftExpressionIsParenthetical(expressionInput, breakPoint)))):
        if (not self.__isOperator(expressionInput[breakPoint])):
          # print("Right Left No Op")
          return self.__splitExpressionParenRightLeftNoOperator(expressionInput, breakPoint)
        else:
          # print("Right Left Op")
          return self.__splitExpressionParenRightLeft(expressionInput, breakPoint)
      if (breakPoint+1 < len(expressionInput) 
        and (self.__rightExpressionIsParentheticalExcludeBreakPoint(expressionInput, breakPoint)
        or self.__rightExpressionIsParentheticalIncludeBreakPoint(expressionInput, breakPoint))):
        if expressionInput[breakPoint] == "(":
          # print("Right No Op")
          return self.__splitExpressionParenRightNoOperator(expressionInput, breakPoint)
        else:
          # print("Right Op")
          return self.__splitExpressionParenRight(expressionInput, breakPoint)
      elif (breakPoint-1 >= 0 and self.__leftExpressionIsParenthetical(expressionInput, breakPoint)):
        if expressionInput[breakPoint].isnumeric():
          # print("Left No Op")
          return self.__splitExpressionParenLeftNoOperator(expressionInput, breakPoint)
        else:
          # print("Left Op")
          return self.__splitExpressionParenLeft(expressionInput, breakPoint)
      # print("No Paren")
      return self.__splitExpressionNoParen(expressionInput, breakPoint)

  def __findValidBreakpoint(self, expressionInput):
    multiplyBreakpoint = 1
    leftExpressionInsideParen = False
    parenCount = 0
    for i in range(len(expressionInput)):
      if expressionInput[i] == "(":
        parenCount += 1
        if i == 0:
          leftExpressionInsideParen = True
      if expressionInput[i] == ")":
        parenCount -= 1
      if leftExpressionInsideParen and parenCount == 0 and multiplyBreakpoint == 1:
        multiplyBreakpoint = i+1
      if parenCount == 0 and (expressionInput[i] == "+" or expressionInput[i] == "-"):
        return i
    return multiplyBreakpoint

  def __splitExpressionParenRightNoOperator(self, expressionInput, breakPoint):
    if expressionInput[-1] == ")":
      # print("Here Here")
      return self.factory.CreateExpression(
        self.__buildExpressionTree(expressionInput[:breakPoint]), 
        "*", 
        self.__buildExpressionTree(expressionInput[breakPoint+1:-1]))
    return self.factory.CreateExpression(
      self.__buildExpressionTree(expressionInput[:breakPoint+1]), 
      "*", 
      self.__buildExpressionTree(expressionInput[breakPoint+1:]))

  def __splitExpressionParenRight(self, expressionInput, breakPoint):
    if expressionInput[-1] == ")": 
      return self.factory.CreateExpression(
        self.__buildExpressionTree(expressionInput[:breakPoint]), 
        expressionInput[breakPoint], 
        self.__buildExpressionTree(expressionInput[breakPoint+2:-1]))
    return self.__splitExpressionNoParen(expressionInput, breakPoint)

  def __splitExpressionNoParen(self, expressionInput, breakPoint):
    return self.factory.CreateExpression(
      self.__buildExpressionTree(expressionInput[:breakPoint]), 
      expressionInput[breakPoint], 
      self.__buildExpressionTree(expressionInput[breakPoint+1:]))

  def __splitExpressionParenLeft(self, expressionInput, breakPoint):
    return self.factory.CreateExpression(
      self.__buildExpressionTree(expressionInput[1:breakPoint-1]), 
      expressionInput[breakPoint], 
      self.__buildExpressionTree(expressionInput[breakPoint+1:]))

  def __splitExpressionParenLeftNoOperator(self, expressionInput, breakPoint):
    return self.factory.CreateExpression(
      self.__buildExpressionTree(expressionInput[1:breakPoint-1]), 
      "*", 
      self.__buildExpressionTree(expressionInput[breakPoint:]))
  
  def __splitExpressionParenRightLeft(self, expressionInput, breakPoint):
    if expressionInput[-1] == ")":
      return self.factory.CreateExpression(
        self.__buildExpressionTree(expressionInput[1:breakPoint-1]), 
        expressionInput[breakPoint], 
        self.__buildExpressionTree(expressionInput[breakPoint+2:-1]))
    return self.__splitExpressionParenLeft(expressionInput, breakPoint)

  def __splitExpressionParenRightLeftNoOperator(self, expressionInput, breakPoint):
    if expressionInput[-1] == ")":
      return self.factory.CreateExpression(
        self.__buildExpressionTree(expressionInput[1:breakPoint-1]), 
        "*", 
        self.__buildExpressionTree(expressionInput[breakPoint+1:-1]))
    return self.__splitExpressionParenLeftNoOperator(expressionInput, breakPoint)

  def __isOperator(self, char):
    return char == "+" or char == "-" or char == "*" or char == "/"

  def __leftExpressionIsParenthetical(self, expressionInput, breakPoint):
    if expressionInput[0] != "(":
      return False
    hasOpenedParen = False
    parenCount = 0
    for i in range(breakPoint - 1):
      if expressionInput[i] == "(":
        hasOpenedParen = True
        parenCount += 1
      if expressionInput[i] == ")":
        parenCount -= 1
        if parenCount == 0:
          return False
    return hasOpenedParen
  
  def __rightExpressionIsParentheticalIncludeBreakPoint(self, expressionInput, breakPoint):
    if expressionInput[breakPoint] != "(":
      return False
    hasOpenedParen = False
    parenCount = 0
    for i in range(breakPoint, len(expressionInput) - 1):
      if expressionInput[i] == "(":
        hasOpenedParen = True
        parenCount += 1
      if expressionInput[i] == ")":
        parenCount -= 1
        if parenCount == 0:
          return False
    return hasOpenedParen
  
  def __rightExpressionIsParentheticalExcludeBreakPoint(self, expressionInput, breakPoint):
    if expressionInput[breakPoint+1] != "(":
      return False
    hasOpenedParen = False
    parenCount = 0
    for i in range(breakPoint, len(expressionInput) - 1):
      if expressionInput[i] == "(":
        hasOpenedParen = True
        parenCount += 1
      if expressionInput[i] == ")":
        parenCount -= 1
        if parenCount == 0:
          return False
    return hasOpenedParen

  def __init__(self, inputExpression):
    self.fullExpression = inputExpression.replace(" ", "")


