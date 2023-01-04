import math

# math.sqrt()

def my_function(input_value):
    if (type(input_value) == float):
        raise TypeError("Invalid Value")
    if not input_value:
        raise TypeError("Empty input")
    else:
        return math.sqrt(input_value)
    