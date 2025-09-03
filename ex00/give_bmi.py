import numpy as np

# checks if lst is a list of int or float and not empty
def check_input(lst: list[int | float]) -> bool:
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True


def is_positive_number(num: int | float) -> bool:
    return num > 0


def are_all_positive_numbers(lst: list[int | float]) -> bool:
    for item in lst:
        if not is_positive_number(item):
            return False
    return True


def is_integer(num: int) -> bool:
    return isinstance(num, int)


# checks if two lists have the same length
def check_lists_length(lst1: list, lst2: list) -> bool:
    return len(lst1) == len(lst2)


# checks if two lists have the same length and are valid
def check_lists(
        height: list[int | float],
        weight: list[int | float]
        ) -> bool:
    return (check_input(height)
            and check_input(weight)
            and check_lists_length(height, weight)
            and are_all_positive_numbers(height)
            and are_all_positive_numbers(weight))


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    
    if check_lists(height, weight) is False:
        raise ValueError("Invalid input")
    
    height_np = np.array(height)
    weight_np = np.array(weight)
    bmi_np = weight_np / (height_np ** 2)

    return bmi_np.tolist()


def apply_limit(
        bmi: list[int | float],
        limit: int
        ) -> list[bool]:
    if check_input(bmi) is False or is_integer(limit) is False:
        raise ValueError("Invalid input")


def main():
    pass


if __name__ == "__main__":
    main()
