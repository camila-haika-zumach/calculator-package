# Calculator Package

The Calculator package provides a set of mathematical operations that can be performed on a memory value. It supports addition, subtraction, multiplication, division, and calculation of nth roots.

## Installation

You can install the Calculator package using pip:

```shell
pip install -i https://test.pypi.org/simple/ mycalculator-chz==2.1.0
```


## Usage

```python
from calculator_package.calculator import Calculator

# Create a calculator object
calculator = Calculator()

# Perform calculations
result = calculator.add(2)
print(result)  # Output: 2

result = calculator.subtract(1)
print(result)  # Output: 1

result = calculator.multiply(3)
print(result)  # Output: 3

result = calculator.divide(2)
print(result)  # Output: 1.5

result = calculator.nth_root(16, 2)
print(result)  # Output: 4

# Retrieve the current value from memory
memory_value = calculator.recall_memory()
print(memory_value)  # Output: 4

# Clear the memory
calculator.clear_memory()
```

## Testing

The Calculator package includes unit tests that can be run using pytest. To run the tests, follow these steps:

1. Install pytest if you haven't already:

```shell
pip install pytest
```

2. Navigate to the root directory of the Calculator package.

3. Run the following command:

```shell
pytest
```

The tests will be executed, and the results will be displayed in the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
The MIT License (MIT)

Copyright (c) 2023 Camila Haika Zumach

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
