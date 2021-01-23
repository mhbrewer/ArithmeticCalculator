import unittest
from RawExpression import RawExpression

class TestRawExpressionIsValid(unittest.TestCase):
  def test_IsValid_1Plus1_Returns_True(self):
    # Arrange
    entireExpression = RawExpression("1+1")
    # Act
    actual = entireExpression.isValid()
    expected = True
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_LParen1Plus1RParen_Returns_True(self):
    # Arrange
    entireExpression = RawExpression("(1+1)")
    # Act
    actual = entireExpression.isValid()
    expected = True
    # Assert
    self.assertEqual(actual, expected)

class TestRawExpressionIsNotValid(unittest.TestCase):
  def test_IsValid_1Plus_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1Plus1Plus_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+1+")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1Plus1Times_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+1*")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_Plus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_Plus1Plus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("+1+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
