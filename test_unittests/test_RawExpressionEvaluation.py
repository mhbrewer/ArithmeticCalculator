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
  
class TestComplexRawExpression(unittest.TestCase):
  def test_Evaluate_1Plus1Plus1_Returns_3(self):
    # Arrange
    entireExpression = RawExpression("1+1+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 3
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1Plus1Plus1Plus1_Returns_4(self):
    # Arrange
    entireExpression = RawExpression("1+1+1+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 4
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2Times2Plus3_Returns_7(self):
    # Arrange
    entireExpression = RawExpression("2*2+3")
    # Act
    actual = entireExpression.evaluate()
    expected = 7
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2Plus2Times3_Returns_8(self):
    # Arrange
    entireExpression = RawExpression("2+2*3")
    # Act
    actual = entireExpression.evaluate()
    expected = 8
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1Times2Times2Plus3_Returns_7(self):
    # Arrange
    entireExpression = RawExpression("1*2*2+3")
    # Act
    actual = entireExpression.evaluate()
    expected = 7
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1Times2Times2Minus3_Returns_1(self):
    # Arrange
    entireExpression = RawExpression("1*2*2-3")
    # Act
    actual = entireExpression.evaluate()
    expected = 1
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2TimesLParen2Plus3RParen_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("2*(2+3)")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2LParen2Plus3RParen_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("2(2+3)")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_LParen2Plus3RParenTimes2_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("(2+3)*2")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_LParen2Plus3RParen2_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("(2+3)2")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_TwoParentheticalsTimes_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("(2+3)*(1+1)")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_TwoParentheticalsNoTimes_Returns_10(self):
    # Arrange
    entireExpression = RawExpression("(2+3)(1+1)")
    # Act
    actual = entireExpression.evaluate()
    expected = 10
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1PlusParentheticalPlus1_Returns_7(self):
    # Arrange
    entireExpression = RawExpression("1+(2+3)+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 7
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_2ParentheticalPlus1_Returns_11(self):
    # Arrange
    entireExpression = RawExpression("2(2+3)+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 11
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_ParentheticalPlusParentheticalPlus1_Returns_8(self):
    # Arrange
    entireExpression = RawExpression("(1+1)+(2+3)+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 8
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_ParentheticalParentheticalPlus1_Returns_11(self):
    # Arrange
    entireExpression = RawExpression("(1+1)(2+3)+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 11
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_1PlusParentheticalParenthetical_Returns_11(self):
    # Arrange
    entireExpression = RawExpression("1+(1+1)(2+3)")
    # Act
    actual = entireExpression.evaluate()
    expected = 11
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_MiscellaneousComplexExpression_Returns_24(self):
    # Arrange
    entireExpression = RawExpression("3*((2+3)-4)*(2+1)(1+1)+5+2/2")
    # Act
    actual = entireExpression.evaluate()
    expected = 24
    # Assert
    self.assertEqual(actual, expected)
  
  def test_Evaluate_MiscellaneousComplexExpressionWithSpaces_Returns_24(self):
    # Arrange
    entireExpression = RawExpression("3* (    (2+3)-4)*(2+1)(1+1)+5+2/ 2")
    # Act
    actual = entireExpression.evaluate()
    expected = 24
    # Assert
    self.assertEqual(actual, expected)






