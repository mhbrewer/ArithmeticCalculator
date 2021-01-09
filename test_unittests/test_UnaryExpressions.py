import unittest
from UnaryExpressions import SingleNumberExpression

class TestSingleNumberExpression(unittest.TestCase):
  def test_Input_1_Returns_1(self):
    # Arrange
    num1 = 1
    unaryExpression = SingleNumberExpression(num1)
    # Act
    actual = unaryExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)