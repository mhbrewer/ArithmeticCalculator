from multipledispatch import dispatch
from UnaryExpressions import SingleNumberExpression
from IExpression import IExpression

class IBinaryExpression(IExpression):
  leftExpression = SingleNumberExpression(0)
  rightExpression = SingleNumberExpression(0)

  @dispatch(IExpression, IExpression)
  def __init__(self, inputLeftExpression, inputRightExpression):
    self.leftExpression = inputLeftExpression
    self.rightExpression = inputRightExpression
  
  def evaluate(self):
    pass

class AdditionExpression(IBinaryExpression):
  def evaluate(self):
    return self.leftExpression.evaluate() + self.rightExpression.evaluate()

class SubtractionExpression(IBinaryExpression):
  def evaluate(self):
    return self.leftExpression.evaluate() - self.rightExpression.evaluate()

class MultiplicationExpression(IBinaryExpression):
  def evaluate(self):
    return self.leftExpression.evaluate() * self.rightExpression.evaluate()

class DivisionExpression(IBinaryExpression):
  def evaluate(self):
    return self.leftExpression.evaluate() / self.rightExpression.evaluate()


