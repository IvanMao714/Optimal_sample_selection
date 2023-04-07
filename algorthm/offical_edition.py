import itertools
from random import sample
from typing import List


def combine(choosen_letter, n, k, s):
    print(f"===========================Combine Function===============================")
    combinations = []
    print(f"--------------------------situation----------------------------")
    middle_letters = choosen_letter[:n - k + s]
    middle_combinations = list(itertools.combinations(middle_letters, s))
    tail_letters = choosen_letter[n - k + s:]
    tail_combinations = list(itertools.combinations(tail_letters, k - s))
    print(middle_combinations, tail_combinations)
    for middle_combination in middle_combinations:
        for tail_combination in tail_combinations:
            temp = list(middle_combination) + list(tail_combination)
            print("temp" + str(temp))
            combinations.append(list(middle_combination) + list(tail_combination))
    print("---------------------------final combination-------------------------")
    for combination in combinations:
        print(combination)
    print(len(combinations))
    return combinations


def select(combinations: list, validation_sets: list) -> list:
    """
    Selects valid combinations from a list of combinations based on a list of validation sets.
    :param combinations: A list of combinations to be validated.
    :param validation_sets: A list of validation sets to validate the combinations against.
    :return: A list of valid combinations.
    """
    valid_combinations = []

    while (len(validation_sets) != 0):
        combination = statistic(combinations, validation_sets)
        flag = 0
        for validation_set in validation_sets:
            if set(validation_set).issubset(set(combination)):
                flag = 1

        validation_sets = [s for s in validation_sets if not set(s).issubset(set(combination))]
        if flag == 1:
            valid_combinations.append(combination)
            combinations.remove(combination)

    print(valid_combinations)
    print(len(valid_combinations))
    return valid_combinations


def statistic(combinations: list, validation_sets: list) -> list:
    """
    Finds the combination that satisfies the most validation sets.
    :param combinations: A list of combinations to be validated.
    :param validation_sets: A list of validation sets to validate the combinations against.
    :return: The combination that satisfies the most validation sets.
    """
    max_count = 0
    max_list = []
    for combination in combinations:
        count = 0
        for validation_set in validation_sets:
            if set(validation_set).issubset(set(combination)):
                count += 1
        if count > max_count:
            max_count = count
            max_list = combination
    return max_list


def statistic_reverse(combinations: list, validation_sets: list) -> list:
    """
    Finds the validation set that satisfies the most combinations.
    :param combinations: A list of combinations to be validated.
    :param validation_sets: A list of validation sets to validate the combinations against.
    :return: The validation set that satisfies the most combinations.
    """
    max_count = 0
    max_list = []
    for validation_set in validation_sets:
        count = 0
        for combination in combinations:
            if set(validation_set).issubset(set(combination)):
                combinations.remove(combination)
                count += 1
        if count > max_count:
            max_count = count
            max_list = validation_set
    return max_list


def remove_duplicate_rows(arr: List[List[int]]) -> List[List[int]]:
    """
    Removes duplicate rows from a 2D list of integers.
    :param arr: The 2D list of integers to remove duplicates from.
    :return: A new 2D list with duplicate rows removed.
    """
    unique_rows = []
    seen = set()

    for row in arr:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(list(row_tuple))

    return unique_rows


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(1, m + 1))
    chosen_letter = sample(potential_letter, n)
    chosen_letter.sort()

    combinations = list(itertools.combinations(chosen_letter, k))

    validation_sets = []
    tmp_sets = list(itertools.combinations(chosen_letter, j))
    if j == s:
        result = select(combinations, tmp_sets)
    else:
        for tmp_set in tmp_sets:
            small = list((itertools.combinations(tmp_set, s)))
            small.sort()
            d = statistic_reverse(tmp_sets, small)
            validation_sets.append(d)
        validation_sets = remove_duplicate_rows(validation_sets)


        result = select(combinations, validation_sets)
    return result


if __name__ == '__main__':
    # search(45, 10, 6, 6, 4)
    # search(45, 9, 6, 4, 4)
    search(45, 10, 6, 6, 4)
    search(45, 7, 6, 5, 5)
