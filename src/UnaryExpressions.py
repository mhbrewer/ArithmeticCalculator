from IExpression import IExpression

class IUnaryExpression(IExpression):
  value = 0

  def __init__(self, inputValue):
    self.value = inputValue

  def evaluate(self):
    pass

class SingleNumberExpression(IUnaryExpression):
  def evaluate(self) -> float:
    return self.value
  