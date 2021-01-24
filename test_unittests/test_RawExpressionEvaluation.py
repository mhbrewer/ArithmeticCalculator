import unittest
from RawExpression import RawExpression

class TestSimpleRawExpression(unittest.TestCase):
  def test_Evaluate_1Plus1_Returns_2(self):
    # Arrange
    entireExpression = RawExpression("1+1")
    # Act
    actual = entireExpression.evaluate()
    expected = 2
    # Assert
    self.assertEqual(actual, expected)