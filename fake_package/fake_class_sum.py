class class_sum():
    
    """Class to sum two numbers.

    :param float x: First number.
    :param float y: Second number.
    """
    
    def __init__(self, x: float, y: float) -> float:
        """The constructor."""
        self.x=x
        self.y=y
        self.summed=self.x+self.y

    def sum(self, x: float,y: float) -> float:
        """Sums two different numbers

        .. WARNING::
            If one of the inputs is not a number, then it doesn't make any sense.

        :param float x: First number.
        :param float y: Second number.
        """
        return x+y

