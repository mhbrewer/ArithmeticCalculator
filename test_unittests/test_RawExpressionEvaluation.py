import unittest
from RawExpression import RawExpression

class TestBinaryRawExpression(unittest.TestCase):
  def test_Evaluate_1Plus1_Returns_2(self):
    # Arrange
    entireExpression = RawExpression("1+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1Plus2_Returns_3(self):
    # Arrange
    entireExpression = RawExpression("1+2")
    # Act
    actual = entireExpression.evaluate()
    expected = 3
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2Plus1_Returns_3(self):
    # Arrange
    entireExpression = RawExpression("2+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 3
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2Times1_Returns_2(self):
    # Arrange
    entireExpression = RawExpression("2*1")
    # Act
    actual = entireExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_4Divides2_Returns_2(self):
    # Arrange
    entireExpression = RawExpression("4/2")
    # Act
    actual = entireExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1Minus1_Returns_0(self):
    # Arrange
    entireExpression = RawExpression("1-1")
    # Act
    actual = entireExpression.evaluate()
    expected = 0
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1_Returns_1(self):
    # Arrange
    entireExpression = RawExpression("1")
    # Act
    actual = entireExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)
  
