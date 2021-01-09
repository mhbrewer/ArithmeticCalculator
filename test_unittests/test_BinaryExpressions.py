import unittest
from BinaryExpressions import AdditiveExpression

class TestAdditiveExpression(unittest.TestCase):
  def test_Input_1_1_Returns_2(self):
    # Arrange
    num1 = 1
    num2 = 1
    binaryExpression = AdditiveExpression(num1, num2)
    # Act
    actual = binaryExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Input_2_4_Returns_6(self):
    # Arrange
    num1 = 2
    num2 = 4
    binaryExpression = AdditiveExpression(num1, num2)
    # Act
    actual = binaryExpression.evaluate()
    expected = 6
    # Assert
    self.assertEqual(actual, expected)

