from multipledispatch import dispatch
from IExpression import IExpression
from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import DivisionExpression
from BinaryExpressions import MultiplicationExpression
from UnaryExpressions import SingleNumberExpression

class ExpressionFactory:
  @dispatch(IExpression, str, IExpression)
  def CreateExpression(self, leftNum, operatorSign, rightNum):
    if(operatorSign == "+"):
      return AdditionExpression(leftNum, rightNum)
    if(operatorSign == "-"):
      return SubtractionExpression(leftNum, rightNum)
    if(operatorSign == "/"):
      return DivisionExpression(leftNum, rightNum)
    return MultiplicationExpression(leftNum, rightNum)
  
  @dispatch(int)
  def CreateExpression(self, inputNum):
    return SingleNumberExpression(inputNum)
  
  @dispatch(float)
  def CreateExpression(self, inputNum):
    return SingleNumberExpression(inputNum)