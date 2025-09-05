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
    """Slices a list from start index to end index, \
prints the original and new shapes, and returns the result as a list of lists.

Parameters:
    family (list): The list to be sliced.
    start (int): The starting index for slicing.
    end (int): The ending index for slicing.

Returns:
    list: The sliced list
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

        family_arr = np.array(family)
        print(f"My shape is : {family_arr.shape}")
        sliced_family = family_arr[start:end]
        print(f"My new shape is : {sliced_family.shape}")

        return sliced_family.tolist()

    except (TypeError, ValueError, OverflowError):
        raise
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


# --- TESTS ---


def test_slice_me():
    """Test slice_me function with various cases.

Parameters:
    None

Returns:
    None
    """
    print("=== TESTING SLICE_ME FUNCTION ===")

    family = [
        [1.75, 68.0],
        [1.62, 55.0],
        [1.80, 75.0],
        [1.50, 45.0],
        [1.70, 60.0]
    ]

    # ✅ Slice normal positive
    result = slice_me(family, 0, 2)
    expected = [[1.75, 68.0], [1.62, 55.0]]
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 0:2 passed\n")

    # ✅ Slice with negative indices
    result = slice_me(family, 1, -1)
    expected = [[1.62, 55.0], [1.80, 75.0], [1.50, 45.0]]
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 1:-1 passed\n")

    # ✅ Slice with start equal to end
    result = slice_me(family, 2, 2)
    expected = []
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 2:2 passed\n")

    # ✅ Slice with end greater than list length
    result = slice_me(family, 3, 10)
    expected = [[1.50, 45.0], [1.70, 60.0]]
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 3:10 passed\n")

    # ✅ Slice with negative start and end
    result = slice_me(family, -3, -1)
    expected = [[1.80, 75.0], [1.50, 45.0]]
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice -3:-1 passed\n")

    # ✅ Slice with start greater than end
    result = slice_me(family, 4, 2)
    expected = []
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 4:2 passed\n")

    # ✅ Slice with full range
    result = slice_me(family, 0, len(family))
    expected = family
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 0:len(family) passed\n")

    # ✅ Slice with start and end as zero
    result = slice_me(family, 0, 0)
    expected = []
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice 0:0 passed\n")

    # ✅ Slice with negative start and positive end
    result = slice_me(family, -4, 3)
    expected = [[1.62, 55.0], [1.80, 75.0]]
    if result != expected:
        raise AssertionError(f"Expected {expected}, got {result}")
    print(result)
    print("✅ Slice -4:3 passed:\n")

    # ❌ is not a list
    try:
        result = slice_me("family", 0, 2)
    except TypeError as e:
        print("✅ Not a list detected:", e)
    else:
        raise AssertionError("Not a list: Did not fail as expected")

    # ❌ Empty list
    try:
        result = slice_me([], 0, 2)
    except ValueError as e:
        print("✅ Empty list detected:", e)
    else:
        raise AssertionError("Empty list: Did not fail as expected")

    # ❌ Not a list of lists
    try:
        result = slice_me([[1, 2], 'not a list'], 0, 2)
    except TypeError as e:
        print("✅ Not a list of lists detected:", e)
    else:
        raise AssertionError("Not a list of lists: Did not fail as expected")

    # ❌ Does not contain 2 elements in each list
    try:
        result = slice_me([[1, 2, 3], [4, 12]], 0, 2)
    except ValueError as e:
        print("✅ Does not contain 2 elements in each list detected:", e)
    else:
        raise AssertionError(
            "Each sublist must have 2 elements: Did not fail as expected")

    # ❌ Not a list of numbers
    try:
        result = slice_me([[1, 'a'], [4, 12]], 0, 2)
    except TypeError as e:
        print("✅ Not a list of numbers detected:", e)
    else:
        raise AssertionError("Not a list of numbers: Did not fail as expected")

    # ❌ Not all positive
    try:
        result = slice_me([[1, -2], [4, 12]], 0, 2)
    except ValueError as e:
        print("✅ Not all positive detected:", e)
    else:
        raise AssertionError("Not all positive: Did not fail as expected")

    # ❌ Overflow detected
    try:
        result = slice_me([[np.inf, 2], [4, 12]], 0, 2)
    except OverflowError as e:
        print("✅ Overflow detected:", e)
    else:
        raise AssertionError("Overflow: Did not fail as expected")

    # ❌ Not integers
    try:
        result = slice_me([[1, 2], [4, 12]], 1.5, 2)
    except TypeError as e:
        print("✅ Not integers detected:", e)
    else:
        raise AssertionError("Not integers: Did not fail as expected")


def main():
    """Main function to run tests for give_bmi, apply_limit functions \
and handle test exceptions.

Parameters:
    None

Returns:
    None
    """
    try:
        test_slice_me()
    except AssertionError as ae:
        print(f"❌ {slice_me.__name__} assertion failed: {ae}")
    except Exception as e:
        print(f"❌ unexpected exception: {e}")
    else:
        print(f"\n✅ All tests in {slice_me.__name__} passed successfully.")


if __name__ == "__main__":
    main()
