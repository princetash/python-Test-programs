import math

"""
    Calculates the length of the hypotenuse of a right triangle given the lengths of the other two legs.

    :param a: Length of the first leg.
    :param b: Length of the second leg.
    :return: Length of the hypotenuse.
    :raises ValueError: If inputs are not numeric or if they are negative.
    """


def hypotenuse(a, b):
    # Check if inputs are numeric (int or
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Input values must be numeric.")
        # Check if inputs are non-negative
    elif a < 0 or b < 0:
        raise ValueError("Input values must be non-negative.")

    # Calculate the hypotenuse using the Pythagorean theorem
    return math.sqrt(a**2 + b**2)


print(hypotenuse(3, 4))
