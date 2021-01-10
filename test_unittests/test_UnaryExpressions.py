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
  
  def test_Input_5_Returns_5(self):
    # Arrange
    num1 = 5
    unaryExpression = SingleNumberExpression(num1)
    # Act
    actual = unaryExpression.evaluate()
    expected = 5
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Input_Neg2Point5_Returns_Neg2Point5(self):
    # Arrange
    num1 = -2.5
    unaryExpression = SingleNumberExpression(num1)
    # Act
    actual = unaryExpression.evaluate()
    expected = -2.5
    # Assert
    self.assertEqual(actual, expected)