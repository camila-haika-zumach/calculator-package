import pytest
from calculator_package.calculator import Calculator

# Test cases for the Calculator class

def test_add():
    calculator = Calculator()
    result = calculator.add(5)
    assert result == 5  # Adding 5 to the initial memory value of 0

def test_subtract():
    calculator = Calculator(10)
    result = calculator.subtract(3)
    assert result == 7  # Subtracting 3 from the initial memory value of 10

def test_multiply():
    calculator = Calculator(2)
    result = calculator.multiply(4)
    assert result == 8  # Multiplying the initial memory value of 2 by 4

def test_divide():
    calculator = Calculator(10)
    result = calculator.divide(2)
    assert result == 5  # Dividing the initial memory value of 10 by 2

def test_divide_by_zero():
    calculator = Calculator(10)
    with pytest.raises(ValueError):
        calculator.divide(0)  # Dividing by zero should raise a ValueError

def test_nth_root():
    calculator = Calculator()
    result = calculator.nth_root(16, 2)
    assert result == 4  # Calculating the square root of 16

def test_recall_memory():
    calculator = Calculator(5)
    result = calculator.recall_memory()
    assert result == 5  # Retrieving the value stored in the memory

def test_clear_memory():
    calculator = Calculator(7)
    calculator.clear_memory()
    result = calculator.recall_memory()
    assert result == 0  # Clearing the memory should set it to 0

