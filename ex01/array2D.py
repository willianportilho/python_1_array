import numpy as np


def is_list_type(obj: object) -> bool:
    """Check if the provided object is of list type.

Parameters:
    obj (object): The object to check.

Returns:
    bool: True if the object is a list, False otherwise.
    """
    if not isinstance(obj, list):
        return False
    return True


def is_empty(family: list) -> bool:
    """Check if the provided list is empty.

Parameters:
    family (list): The list to check.

Returns:
    bool: True if the list is empty, False otherwise.
    """
    if len(family) == 0:
        return True
    return False


def is_list_of_lists(family: list) -> bool:
    """Check if the provided list is a list of lists.

Parameters:
    family (list): The list to check.

Returns:
    bool: True if the list is a list of lists, False otherwise.
    """
    for item in family:
        if not is_list_type(item):
            return False
    return True


def has_2_elements(family: list) -> bool:
    """Check if each sublist in the provided list has exactly 2 elements.

Parameters:
    family (list): The list of lists to check.

Returns:
    bool: True if each sublist has 2 elements, False otherwise.
    """
    for item in family:
        if len(item) != 2:
            return False
    return True


def is_list_of_2_numbers(family: list) -> bool:
    """Check if each sublist elements in the family are of type int or float.

Parameters:
    family (list): The list of lists to check.

Returns:
    bool: True if each sublist elements are int or float, False otherwise.
    """
    for item in family:
        for element in item:
            if isinstance(element, (int, float)) is False:
                return False
    return True


def are_all_positive_numbers(family: list) -> bool:
    """Check if each sublist elements in the family are positive numbers.

Parameters:
    family (list): The list of lists to check.

Returns:
    bool: True if each sublist elements are positive numbers, False otherwise.
    """
    for item in family:
        for element in item:
            if element <= 0:
                return False
    return True


def check_overflow(family: list) -> bool:
    """Check if any element in the sublists exceeds the maximum float value.

Parameters:
    family (list): The list of lists to check.

Returns:
    bool: True if any element exceeds the maximum float value, False otherwise.
    """
    for item in family:
        for element in item:
            arr = np.array([element], dtype=np.float64)
            if np.isinf(arr[0]) or np.isnan(arr[0]):
                return True
    return False


def are_start_end_int(start: int, end: int) -> bool:
    """Check if start and end parameters are integers.

Parameters:
    start (int): The start index.
    end (int): The end index.

Returns:
    bool: True if both start and end are integers, False otherwise.
    """
    if isinstance(start, int) is False or isinstance(end, int) is False:
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a list from start index to end index using slicing.

Parameters:
    family (list): The list to be sliced.
    start (int): The starting index for slicing.
    end (int): The ending index for slicing.

Returns:
    list: The sliced portion of the list.
    """
    try:
        if is_list_type(family) is False:
            raise TypeError("family must be a list")
        if is_empty(family) is True:
            raise ValueError("family must not be empty")
        if is_list_of_lists(family) is False:
            raise TypeError("family must be a list of lists")
        if has_2_elements(family) is False:
            raise ValueError("each sublist in family must have 2 elements")
        if is_list_of_2_numbers(family) is False:
            raise TypeError("each sublist elements must be int or float")
        if are_all_positive_numbers(family) is False:
            raise ValueError("each sublist elements must be positive numbers")
        if check_overflow(family) is True:
            raise OverflowError("overflow detected in family elements")
        if are_start_end_int(start, end) is False:
            raise TypeError("start and end must be integers")

        return family[start:end]

    except (TypeError, ValueError, OverflowError):
        raise
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def main():
    """Main function to run tests for give_bmi and apply_limit functions \
and handle test exceptions.

Parameters:
    None

Returns:
    None
    """
    try:
        slice_me([[1.75, 70], [1.80, 80], [1.65, 60]], 4, 2)  # Valid case
    except AssertionError as ae:
        print(f"❌ {slice_me.__name__} assertion failed: {ae}")
    except Exception as e:
        print(f"❌ {slice_me.__name__} unexpected exception: {e}")
    else:
        print(f"✅ All tests in {slice_me.__name__} passed successfully.")


if __name__ == "__main__":
    main()
