from multipledispatch import dispatch
from IExpression import IExpression
from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import DivisionExpression
from BinaryExpressions import MultiplicationExpression
from UnaryExpressions import SingleNumberExpression

class ExpressionFactory:
  @dispatch(IExpression, str, IExpression)
  def CreateExpression(self, leftExp, operatorSign, rightExp):
    if(operatorSign == "+"):
      return AdditionExpression(leftExp, rightExp)
    if(operatorSign == "-"):
      return SubtractionExpression(leftExp, rightExp)
    if(operatorSign == "/"):
      return DivisionExpression(leftExp, rightExp)
    return MultiplicationExpression(leftExp, rightExp)
  
  @dispatch(int)
  def CreateExpression(self, inputNum):
    return SingleNumberExpression(inputNum)
  
  @dispatch(float)
  def CreateExpression(self, inputNum):
    return SingleNumberExpression(inputNum)
  
  @dispatch(str)
  def CreateExpression(self, inputNum):
    if inputNum.isnumeric():
      return SingleNumberExpression(float(inputNum))
    return SingleNumberExpression(0)