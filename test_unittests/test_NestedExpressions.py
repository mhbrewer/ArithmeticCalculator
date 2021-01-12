import unittest
from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import MultiplicationExpression
from BinaryExpressions import DivisionExpression
from UnaryExpressions import SingleNumberExpression

class TestExpressionNesting(unittest.TestCase):
  def test_Multiply_Sum_2_1_And_Sum_1_3_Returns_12(self):
    # Arrange
    leftExpression = AdditionExpression(SingleNumberExpression(2), SingleNumberExpression(1))
    rightExpression = AdditionExpression(SingleNumberExpression(1), SingleNumberExpression(3))
    entireExpression = MultiplicationExpression(leftExpression, rightExpression)
    # Act
    actual = entireExpression.evaluate()
    expected = 12
    # Assert
    self.assertEqual(actual, expected)

  def test_Add_Product_3_2_And_Sum_1_3_Returns_10(self):
    # Arrange
    leftExpression = MultiplicationExpression(SingleNumberExpression(3), SingleNumberExpression(2))
    rightExpression = AdditionExpression(SingleNumberExpression(1), SingleNumberExpression(3))
    entireExpression = AdditionExpression(leftExpression, rightExpression)
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)

  def test_Divide_Difference_11_1_And_Product_2_5_Returns_1(self):
    # Arrange
    leftExpression = SubtractionExpression(SingleNumberExpression(11), SingleNumberExpression(1))
    rightExpression = MultiplicationExpression(SingleNumberExpression(2), SingleNumberExpression(5))
    entireExpression = DivisionExpression(leftExpression, rightExpression)
    # Act
    actual = entireExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)