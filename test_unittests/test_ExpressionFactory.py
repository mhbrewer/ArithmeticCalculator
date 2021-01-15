import unittest
from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import MultiplicationExpression
from BinaryExpressions import DivisionExpression
from UnaryExpressions import SingleNumberExpression
from ExpressionFactory import ExpressionFactory

class TestAdditionExpressionCreation(unittest.TestCase):
  def test_Create_1_Plus_1_Is_AdditionExpression(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorSign = "+"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = isinstance(binaryExpression, AdditionExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Create_1_Plus_1_Evaluates_2(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorSign = "+"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)

class TestSubtractionExpressionCreation(unittest.TestCase):
  def test_Create_1_Minus_1_Is_SubtractionExpression(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorSign = "-"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = isinstance(binaryExpression, SubtractionExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)

  def test_Create_2_Minus_1_Evaluates_1(self):
    # Arrange
    leftNum = SingleNumberExpression(2)
    operatorSign = "-"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)

class TestDivisionExpressionCreation(unittest.TestCase):  
  def test_Create_1_Divide_1_Is_DivisionExpression(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorSign = "/"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = isinstance(binaryExpression, DivisionExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)

  def test_Create_6_Divide_2_Evaluates_3(self):
    # Arrange
    leftNum = SingleNumberExpression(6)
    operatorSign = "/"
    rightNum = SingleNumberExpression(2)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 3
    # Assert
    self.assertEqual(actual, expected)

class TestMultiplicationExpressionCreation(unittest.TestCase):
  def test_Create_1_Times_1_Is_DivisionExpression(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    operatorSign = "*"
    rightNum = SingleNumberExpression(1)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = isinstance(binaryExpression, MultiplicationExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)

  def test_Create_6_Times_2_Evaluates_12(self):
    # Arrange
    leftNum = SingleNumberExpression(6)
    operatorSign = "*"
    rightNum = SingleNumberExpression(2)
    binaryExpression = ExpressionFactory().CreateExpression(leftNum, operatorSign, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 12
    # Assert
    self.assertEqual(actual, expected)

class TestSingleNumExpressionCreation(unittest.TestCase):
  def test_Create_Int1_Is_SingleNumberExpression(self):
    # Arrange
    inputNum = 1
    expression = ExpressionFactory().CreateExpression(inputNum)
    # Act
    actual = isinstance(expression, SingleNumberExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Create_Float1_Is_SingleNumberExpression(self):
    # Arrange
    inputNum = 1.0
    expression = ExpressionFactory().CreateExpression(inputNum)
    # Act
    actual = isinstance(expression, SingleNumberExpression)
    expected = True
    # Assert
    self.assertEqual(actual, expected)