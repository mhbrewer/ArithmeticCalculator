from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import MultiplicationExpression
from BinaryExpressions import DivisionExpression
from UnaryExpressions import SingleNumberExpression
from ExpressionFactory import ExpressionFactory

class TestExpressionCreation(unittest.TestCase):
  def test_Create_1_Plus_1_Is_AdditionExpression(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorChar = "+"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory(leftNum, operatorChar, rightNum)
    # Act
    actual = isinstance(binaryExpression, AdditionExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)