import unittest
from BinaryExpressions import AdditionExpression
from BinaryExpressions import SubtractionExpression
from BinaryExpressions import MultiplicationExpression
from BinaryExpressions import DivisionExpression
from UnaryExpressions import SingleNumberExpression

class TestAdditionExpression(unittest.TestCase):
  def test_Add_Input_1_1_Returns_2(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    rightNum = SingleNumberExpression(1)
    binaryExpression = AdditionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Add_Input_2_4_Returns_6(self):
    # Arrange
    leftNum = SingleNumberExpression(2)
    rightNum = SingleNumberExpression(4)
    binaryExpression = AdditionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 6
    # Assert
    self.assertEqual(actual, expected)

class TestSubtractionExpression(unittest.TestCase):
  def test_Subtract_Input_1_1_Returns_0(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    rightNum = SingleNumberExpression(1)
    binaryExpression = SubtractionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 0
    # Assert
    self.assertEqual(actual, expected)

  def test_Subtract_Input_Neg2_1_Returns_Neg3(self):
    # Arrange
    leftNum = SingleNumberExpression(-2)
    rightNum = SingleNumberExpression(1)
    binaryExpression = SubtractionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = -3
    # Assert
    self.assertEqual(actual, expected)

  def test_Subtract_Input_1_Neg2_Returns_3(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    rightNum = SingleNumberExpression(-2)
    binaryExpression = SubtractionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 3
    # Assert
    self.assertEqual(actual, expected)

class TestMultiplicationExpression(unittest.TestCase):
  def test_Multiply_Input_1_1_Returns_1(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    rightNum = SingleNumberExpression(1)
    binaryExpression = MultiplicationExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)

  def test_Multiply_Input_3_4_Returns_12(self):
    # Arrange
    leftNum = SingleNumberExpression(3)
    rightNum = SingleNumberExpression(4)
    binaryExpression = MultiplicationExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 12
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Multiply_Input_Neg3_4_Returns_12(self):
    # Arrange
    leftNum = SingleNumberExpression(-3)
    rightNum = SingleNumberExpression(4)
    binaryExpression = MultiplicationExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = -12
    # Assert
    self.assertEqual(actual, expected)

class TestMultiplicationExpression(unittest.TestCase):
  def test_Divide_Input_1_1_Returns_1(self):
    # Arrange
    leftNum = SingleNumberExpression(1)
    rightNum = SingleNumberExpression(1)
    binaryExpression = DivisionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Divide_Input_4_2_Returns_2(self):
    # Arrange
    leftNum = SingleNumberExpression(4)
    rightNum = SingleNumberExpression(2)
    binaryExpression = DivisionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Divide_Input_2_4_Returns_Point5(self):
    # Arrange
    leftNum = SingleNumberExpression(2)
    rightNum = SingleNumberExpression(4)
    binaryExpression = DivisionExpression(leftNum, rightNum)
    # Act
    actual = binaryExpression.evaluate()
    expected = 0.5
    # Assert
    self.assertEqual(actual, expected)
  