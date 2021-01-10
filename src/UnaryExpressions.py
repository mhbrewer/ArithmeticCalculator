

class SingleNumberExpression:
  value = 0

  def __init__(self, inputValue):
    self.value = inputValue

  def evaluate(self) -> float:
    return self.value
  