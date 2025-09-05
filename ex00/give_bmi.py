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


# --- Test functions -- #


def test_give_bmi():
    """Tests for the give_bmi function.

Parameters:
    None

Returns:
    None
    """
    print("=== TESTING GIVE BMI FUNCTION ===")
    # ✅ Valid case
    heights = [1.75, 1.80, 1.65]
    weights = [70, 80, 60]
    bmi = give_bmi(heights, weights)
    if bmi != [22.857142857142858, 24.691358024691358, 22.03856749311295]:
        raise AssertionError("Valid case: BMI calculation is failed")
    print("✅ Valid case passed:", bmi)

    # ❌ Is not a list case
    try:
        give_bmi("not a list", [50])
    except ValueError as e:
        print("✅ Not a list detected:", e)
    else:
        raise AssertionError("Not a list: Did not fail as expected")

    # ❌ Empty list case
    try:
        give_bmi([], [50])
    except ValueError as e:
        print("✅ Empty list detected:", e)
    else:
        raise AssertionError("Empty list: Did not fail as expected")

    # ❌ Non-numeric values case
    try:
        give_bmi([1.8, 'a'], [80, 50])
    except ValueError as e:
        print("✅ Non-numeric values detected:", e)
    else:
        raise AssertionError("Non-numeric values: Did not fail as expected")

    # ❌ Different lengths case
    try:
        give_bmi([1.8, 1.75], [80])
    except ValueError as e:
        print("✅ Different lengths detected:", e)
    else:
        raise AssertionError("Different lengths: Did not fail as expected")

    # ❌ Negative values case
    try:
        give_bmi([1.8, -1.75], [80, 50])
    except ValueError as e:
        print("✅ Negative values detected:", e)
    else:
        raise AssertionError("Negative values: Did not fail as expected")

    # ❌ Overflow case
    try:
        give_bmi([np.inf, 1.75], [80, 50])
    except OverflowError as e:
        print("✅ Overflow detected:", e)
    else:
        raise AssertionError("Overflow: Did not fail as expected")


def test_appy_limit():
    """Tests for the apply_limit function.

Parameters:
    None

Returns:
    None
    """
    print("\n=== TESTING APPLY LIMIT FUNCTION ===")
    bmi = [22.5, 29.0, 15.2]

    # ✅ Valid case
    if apply_limit(bmi, 25) != [False, True, False]:
        raise AssertionError("Valid case: Limit application is failed")

    # ❌ Is not a list case
    try:
        apply_limit("not a list", 25)
    except ValueError as e:
        print("✅ Not a list detected:", e)
    else:
        raise AssertionError("Not a list: Did not fail as expected")

    # ❌ Empty list case
    try:
        apply_limit([], 25)
    except ValueError as e:
        print("✅ Empty list detected:", e)
    else:
        raise AssertionError("Empty list: Did not fail as expected")

    # ❌ Non-numeric values case
    try:
        apply_limit([22.5, 'a'], 25)
    except ValueError as e:
        print("✅ Non-numeric values detected:", e)
    else:
        raise AssertionError("Non-numeric values: Did not fail as expected")

    # ❌ 'limit' is not a integer
    try:
        apply_limit([22.5, 29.0], 25.5)
    except TypeError as e:
        print("✅ 'limit' is not an integer detected:", e)
    else:
        raise AssertionError("'limit' is not an int: Did not fail as expected")

    # ❌ Negative 'limit' case
    try:
        apply_limit([22.5, 29.0], -25)
    except ValueError as e:
        print("✅ Negative 'limit' detected:", e)
    else:
        raise AssertionError("Negative 'limit': Did not fail as expected")

    # ❌ Overflow case for bmi values
    try:
        apply_limit([np.inf, 29.0], 25)
    except OverflowError as e:
        print("✅ Overflow in bmi values detected:", e)
    else:
        raise AssertionError("Overflow in bmi: Did not fail as expected")


def main():
    """Main function to run tests for give_bmi and apply_limit functions \
and handle test exceptions.

Parameters:
    None

Returns:
    None
    """
    tests = [test_give_bmi, test_appy_limit]

    for test_func in tests:
        try:
            test_func()
        except AssertionError as ae:
            print(f"❌ {test_func.__name__} assertion failed: {ae}")
        except Exception as e:
            print(f"❌ {test_func.__name__} unexpected exception: {e}")
        else:
            print(f"✅ All tests in {test_func.__name__} passed successfully.")


if __name__ == "__main__":
    main()
