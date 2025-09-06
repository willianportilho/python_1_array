import numpy as np


def is_instance_of_list(obj: object) -> bool:
    """Checks if the object is an instance of list.

Parameters:
    obj (object): The object to be checked.
Returns:
    bool: True if obj is a list, False otherwise.
    """
    if not isinstance(obj, list):
        return False


def is_numeric_list(lst: list[int | float]) -> bool:
    """Checks if all elements in the list are numeric (int or float).

Parameters:
    lst: list[int | float]: The list to be checked.

Returns:
    bool: True if all elements are numeric, False otherwise.
    """
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True


def is_non_empty_list(lst: list[int | float]) -> bool:
    """Checks if the input is a non-empty list.

Parameters:
    lst: list[int | float]: The list to be checked.

Returns:
    bool: True if lst is a non-empty list, False otherwise.
    """
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    return True


def check_overflow(num: int | float) -> bool:
    """Checks if a number is infinite or NaN.

Parameters:
    num (int | float): The number to be checked.

Returns:
    bool: True if num is infinite or NaN, False otherwise.
    """
    arr = np.array([num], dtype=np.float64)
    if np.isinf(arr[0]) or np.isnan(arr[0]):
        return True
    return False


def is_positive_number(num: int | float) -> bool:
    """Checks if a number is positive.

Parameters:
    num (int | float): The number to be checked.

Returns:
    bool: True if num is positive, False otherwise.
    """
    return num > 0


def are_all_positive_numbers(lst: list[int | float]) -> bool:
    """Checks if all elements in the list are positive numbers.

Parameters:
    lst (list[int | float]): The list to be checked.

Returns:
    bool: True if all elements are positive numbers, False otherwise.
    """
    for item in lst:
        if not is_positive_number(item):
            return False
    return True


def is_int_type(num: int) -> bool:
    """Checks if a number is of integer type.

Parameters:
    num (int): The number to be checked.

Returns:
    bool: True if num is an integer, False otherwise.
    """
    return isinstance(num, int)


def check_lists_length(lst1: list, lst2: list) -> bool:
    """Checks if two lists have the same length.

Parameters:
    lst1 (list): The first list.
    lst2 (list): The second list.

Returns:
    bool: True if both lists have the same length, False otherwise.
    """
    return len(lst1) == len(lst2)


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """Calculates the Body Mass Index (BMI) for each pair of height and weight.

Parameters:
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

Returns:
    list[int | float]: A list of BMI values calculated using the formula:
        BMI = weight / (height ** 2)
    """
    try:
        if is_instance_of_list(height) is False:
            raise ValueError("Height must be a list")
        if is_instance_of_list(weight) is False:
            raise ValueError("Weight must be a list")
        if is_non_empty_list(height) is False:
            raise ValueError("Height list must be non-empty")
        if is_non_empty_list(weight) is False:
            raise ValueError("Weight list must be non-empty")
        if is_numeric_list(height) is False:
            raise ValueError("Height list must contain only numbers")
        if is_numeric_list(weight) is False:
            raise ValueError("Weight list must contain only numbers")
        if check_lists_length(height, weight) is False:
            raise ValueError("The lists must have the same length")
        if are_all_positive_numbers(height) is False:
            raise ValueError("Height values must be positive")
        if are_all_positive_numbers(weight) is False:
            raise ValueError("Weight values must be positive")
        if any(check_overflow(item) for item in height):
            raise OverflowError("Overflow detected in height list")
        if any(check_overflow(item) for item in weight):
            raise OverflowError("Overflow detected in weight list")

        for h in height:
            if check_overflow(h ** 2):
                raise OverflowError("Overflow detected in height squared")
        for w in weight:
            if check_overflow(w):
                raise OverflowError("Overflow detected in weight value")

        height_np = np.array(height)
        weight_np = np.array(weight)
        bmi_np = weight_np / (height_np ** 2)

        return bmi_np.tolist()

    except (ValueError, OverflowError):
        raise
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")


def apply_limit(
        bmi: list[int | float],
        limit: int
        ) -> list[bool]:
    """Applies a limit to the BMI values and returns a list of booleans
indicating whether each BMI value exceeds the limit.

Parameters:
    bmi (list[int | float]): A list of BMI values.
    limit (int): The BMI limit to compare against.

Returns:
    list[bool]: A list of booleans where each element is True if the
        corresponding BMI value exceeds the limit, and False otherwise.
    """
    try:
        if is_instance_of_list(bmi) is False:
            raise ValueError("BMI must be a list")
        if is_non_empty_list(bmi) is False:
            raise ValueError("BMI list must be non-empty")
        if is_numeric_list(bmi) is False:
            raise ValueError("BMI list must contain only numbers")
        if are_all_positive_numbers(bmi) is False:
            raise ValueError("Values must be positive")
        if is_int_type(limit) is False:
            raise TypeError("Invalid type (limit must be an integer)")
        if is_positive_number(limit) is False:
            raise ValueError("Limit must be a positive integer")
        if check_overflow(limit):
            raise OverflowError("Overflow detected in limit value")

        bmi_np = np.array(bmi)

        if any(check_overflow(item) for item in bmi_np):
            raise OverflowError("Overflow detected in BMI list")

        return (bmi_np > limit).tolist()

    except (ValueError, TypeError, OverflowError):
        raise
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")
