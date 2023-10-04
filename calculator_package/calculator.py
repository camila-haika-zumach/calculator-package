class Calculator:
    def __init__(self, starting_number=0):
        self.memory = starting_number

    def add(self, num2: float) -> float:
        """
        Adds a number to the current memory value and returns the result.

        Args:
            num2 (float): The number to be added to the current memory value.

        Returns:
            float: The result of adding the number to the current memory value.

        """
        result = self.memory + num2
        self.memory = result
        return result

    def subtract(self, num2: float) -> float:
        """
        Subtracts a number from the current memory value and returns the result.

        Args:
            num2 (float): The number to be subtracted from the current memory value.

        Returns:
            float: The result of subtracting the number from the current memory value.

        """
        result = self.memory - num2
        self.memory = result
        return result

    def multiply(self, num2: float) -> float:
        """
        Multiplies the current memory value by a given number and returns the result.

        Args:
            num2 (float): The number to multiply the current memory value by.

        Returns:
            float: The result of multiplying the current memory value by the given number.

        """
        result = self.memory * num2
        self.memory = result
        return result

    def divide(self, num2: float) -> float:
        """
        Divides the current memory value by a given number and returns the result.

        Args:
            num2 (float): The number to divide the current memory value by.

        Returns:
            float: The result of dividing the current memory value by the given number.

        Raises:
            ValueError: If the given number is zero.

        """
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")

        result = self.memory / num2
        self.memory = result
        return result

    def nth_root(self, number: float, n: int) -> float:
        """
        Calculates the nth root of a number and stores the result in the memory attribute.

        Args:
            number (float): The number for which to calculate the nth root.
            n (int): The root degree.

        Returns:
            float: The nth root of the number, rounded to two decimal places or as an integer.

        Raises:
            ValueError: If the number is negative and n is even, or if n is zero.

        """
        if number < 0 and n % 2 == 0:
            raise ValueError("Nth root is not defined for negative numbers when n is even.")
        if n == 0:
            raise ValueError("Nth root is not defined for n = 0.")
        if number == 0:
            self.memory = 0.0
            return self.memory

        result_prev = number
        result = number / n  # Initial guess for the root

        while abs(result - result_prev) > 0.0001:  # Specify the desired precision here
            result_prev = result
            result = ((n - 1) * result + (number / (result ** (n - 1)))) / n

        rounded_result = round(result, 2) if result % 1 != 0 else int(result)

        self.memory = rounded_result
        return self.memory

    def recall_memory(self) -> float:
        """
        Retrieves the current value stored in the memory.

        Returns:
            float: The value stored in the memory.

        """
        return self.memory

    def clear_memory(self) -> float:
        self.memory = 0
