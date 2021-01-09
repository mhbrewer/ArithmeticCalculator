

class AdditiveExpression:
  leftExpression = 0
  rightExpression = 0

  def __init__(self, num1, num2):
    self.leftExpression = num1
    self.rightExpression = num2
  
  def evaluate(self):
    return self.leftExpression + self.rightExpression