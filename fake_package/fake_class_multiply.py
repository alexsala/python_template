class class_multiply:

    """Class to multiply two numbers.

    :param float x: First number.
    :param float y: Second number.
    """

    def __init__(self, x: float, y: float) -> float:
        """The constructor."""
        self.x = x
        self.y = y
        self.multiplied = self.x * self.y

    def multiply(self, x: float, y: float) -> float:
        """Mutliplies two different numbers

        .. WARNING::
            If one of the two numbers is zero, the result will be zero.

        .. WARNING::
            If one of the inputs is not a number, then it doesn't make any sense.

        :param float x: First number.
        :param float y: Second number.
        """
        return x * y
