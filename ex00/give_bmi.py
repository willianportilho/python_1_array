import numpy as np


# checks if lst is a list of int or float and not empty
def is_numeric_list(lst: list[int | float]) -> bool:
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True


def is_nonempty_list(lst: list[int | float]) -> bool:
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    return True


def check_overflow(num: int | float) -> bool:
    arr = np.array([num], dtype=np.float64)
    if np.isinf(arr[0]) or np.isnan(arr[0]):
        return True
    return False


def is_positive_number(num: int | float) -> bool:
    return num > 0


def are_all_positive_numbers(lst: list[int | float]) -> bool:
    for item in lst:
        if not is_positive_number(item):
            return False
    return True


def is_int_type(num: int) -> bool:
    return isinstance(num, int)


# checks if two lists have the same length
def check_lists_length(lst1: list, lst2: list) -> bool:
    return len(lst1) == len(lst2)


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:

    try:
        if is_nonempty_list(height) is False:
            raise ValueError("Height list must be non-empty")
        if is_nonempty_list(weight) is False:
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

    try:
        if is_nonempty_list(bmi) is False:
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


def main():
    pass


if __name__ == "__main__":
    main()
