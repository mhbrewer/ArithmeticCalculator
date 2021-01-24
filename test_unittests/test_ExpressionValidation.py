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
  
  def test_IsValid_PlusLParenConfiguration_Returns_True(self):
    # Arrange
    entireExpression = RawExpression("1+(1+1)")
    # Act
    actual = entireExpression.isValid()
    expected = True
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_RParenPlusConfiguration_Returns_True(self):
    # Arrange
    entireExpression = RawExpression("(1+1)+1")
    # Act
    actual = entireExpression.isValid()
    expected = True
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_NestedParenConfiguration_Returns_True(self):
    # Arrange
    entireExpression = RawExpression("((1+1)+1)")
    # Act
    actual = entireExpression.isValid()
    expected = True
    # Assert
    self.assertEqual(actual, expected)

class TestRawExpressionInvalidEndpoints(unittest.TestCase):
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
  
  def test_IsValid_RParenStart_Returns_False(self):
    # Arrange
    entireExpression = RawExpression(")1+1)")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_LParenEnd_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("(1+1(")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)

class TestRawExpressionInvalidChars(unittest.TestCase):
  def test_IsValid_aPlus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("a+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1Plusa_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+a")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1PlusaPlus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+a+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1PlusaPlus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+b+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1hello1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1hello1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)

class TestRawExpressionInvalidParenthesis(unittest.TestCase):
  def test_IsValid_LParen1Plus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("(1+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1Plus1RParen_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+1)")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_BackwardsParens_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+)1+1(+1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)

class TestRawExpressionInvalidCharArrangement(unittest.TestCase):
  def test_IsValid_EmptyString_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)

  def test_IsValid_1PlusPlus1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1++1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_1PlusTimes1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+*1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_ParenAroundTimes_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+(*)1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_ParenAroundTimes1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+(*1)1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_ParenAroundTimes1_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+(1*)1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)
  
  def test_IsValid_EmptyParens_Returns_False(self):
    # Arrange
    entireExpression = RawExpression("1+()1")
    # Act
    actual = entireExpression.isValid()
    expected = False
    # Assert
    self.assertEqual(actual, expected)








  