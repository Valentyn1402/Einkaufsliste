import re 
from tkinter import messagebox
from fractions import Fraction

# pattern for exception handling 
PATTERN = r"^[a-zA-Z']+$"

class InvalidInputException(Exception):
    """Custom exception for invalid input strings."""
    pass

def check_matching_pattern(input_string: str):
    # Define the regex pattern to match all alphabetical letters (capital and uncapitalized) and the character '''
    
    # Check if the input string matches the regex pattern
    if not re.match(PATTERN, input_string):
        # If it does not match, raise an InvalidInputException
        raise InvalidInputException(f"Invalid input: '{input_string}' does not match the required pattern.")
    
    return True

def validate_input_string(input_string: str):
    try:
        check_matching_pattern("HelloWorld")
        print("Input string is valid.")
    except InvalidInputException as e:
        print(e)
        messagebox.showwarning("Warning", "Do not use any special characters or numbers!")

def validate_input_number(input_number: str):
    def try_parse_int(s):
        try:
            return int(s)
        except ValueError:
            return None

    def try_parse_fraction(s):
        try:
            numerator, denominator = s.split("/")
            return float(numerator) / float(denominator)
        except ValueError:
            return None

    def try_parse_float(s):
        try:
            return float(s)
        except ValueError:
            return None

    # Attempt to parse as an integer
    result = try_parse_int(input_number)
    if result is not None:
        return result

    # Attempt to parse as a fraction
    result = try_parse_fraction(input_number)
    if result is not None:
        return result

    # Attempt to parse as a float
    result = try_parse_float(input_number)
    if result is not None:
        return result

    # If all parsing attempts fail, raise a ValueError
    raise ValueError(f"Invalid input: unable to parse '{input_number}' as a number")

