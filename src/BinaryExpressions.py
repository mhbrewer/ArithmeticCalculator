from UnaryExpressions import SingleNumberExpression

class AdditionExpression:
  leftExpression = SingleNumberExpression(0)
  rightExpression = SingleNumberExpression(0)

  def __init__(self, inputLeftExpression, inputRightExpression):
    self.leftExpression = inputLeftExpression
    self.rightExpression = inputRightExpression
  
  def evaluate(self):
    return self.leftExpression.evaluate() + self.rightExpression.evaluate()

class SubtractionExpression:
  leftExpression = SingleNumberExpression(0)
  rightExpression = SingleNumberExpression(0)

  def __init__(self, inputLeftExpression, inputRightExpression):
    self.leftExpression = inputLeftExpression
    self.rightExpression = inputRightExpression
  
  def evaluate(self):
    return self.leftExpression.evaluate() - self.rightExpression.evaluate()

class MultiplicationExpression:
  leftExpression = SingleNumberExpression(0)
  rightExpression = SingleNumberExpression(0)

  def __init__(self, inputLeftExpression, inputRightExpression):
    self.leftExpression = inputLeftExpression
    self.rightExpression = inputRightExpression

  def evaluate(self):
    return self.leftExpression.evaluate() * self.rightExpression.evaluate()

class DivisionExpression:
  leftExpression = SingleNumberExpression(0)
  rightExpression = SingleNumberExpression(0)

  def __init__(self, inputLeftExpression, inputRightExpression):
    self.leftExpression = inputLeftExpression
    self.rightExpression = inputRightExpression

  def evaluate(self):
    return self.leftExpression.evaluate() / self.rightExpression.evaluate()


