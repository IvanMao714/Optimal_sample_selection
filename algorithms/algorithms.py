import itertools
import math
from random import sample
from typing import List
from tqdm import tqdm
import time


def select(n, combinations: list, validation_sets: list) -> list:
    """
    Selects valid combinations from a list of combinations based on a list of validation sets.
    :param combinations: A list of combinations to be validated.
    :param validation_sets: A list of validation sets to validate the combinations against.
    :return: A list of valid combinations.
    """
    valid_combinations = ""
    total_len_validation_sets = len(validation_sets)
    valid_combinations_length = 0
    time1 = time.time()

    with tqdm(total=total_len_validation_sets) as pbar:
        while (len(validation_sets) != 0):
            len_validation_sets = len(validation_sets)
            r_combinations = statistic(n, combinations, validation_sets)
            for combination in r_combinations:
                validation_sets = [s for s in validation_sets if not set(s).issubset(set(combination))]

                valid_combinations = valid_combinations + str(combination) + "\n"
                valid_combinations_length = valid_combinations_length + 1
                combinations.remove(combination)
            pbar.update(len_validation_sets - len(validation_sets))
            # gc.collect()
    print(str(valid_combinations))
    print(valid_combinations_length)
    time2 = time.time()
    valid_combinations = valid_combinations + "There are " + str(valid_combinations_length) + " combinations need to collected \nTime cost is " + str(time2-time1)
    return valid_combinations


def statistic(n, combinations: list, validation_sets: list) -> list:
    """
    Finds the combination that satisfies the most validation sets.
    :param combinations: A list of combinations to be validated.
    :param validation_sets: A list of validation sets to validate the combinations against.
    :return: The combination that satisfies the most validation sets.
    """



    max_count = 0
    max_list = []
    max = []
    r_combinations = []
    repeat = 0
    # validation_sets_segment = []
    validation_sets_len = len(validation_sets)

    if validation_sets_len > 400:

        validation_sets_segment = validation_sets[:(validation_sets_len//3)]
    else:
        validation_sets_segment = validation_sets


    for combination in combinations:

        count = 0

        for validation_set in validation_sets_segment:
            if set(validation_set).issubset(set(combination)):
                count += 1
        if count >= max_count:
            max_count = count

        if count == max_count:
            repeat = 1 + repeat
            max = combination
            max_list.append(combination)
        if repeat >= int(len(combinations) / 5) and n >= 14 :
            times = math.ceil(repeat / 125) + 1
            for time in range(1, int(times)):
                r_combinations.append(max_list[int(len(max_list) / times * time)])
            return r_combinations
        # gc.collect()
    return [max]


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
        if count >= max_count:
            max_count = count
            max_list = validation_set
        # gc.collect()
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


def search(chosen_letter, k, j, s):
    # potential_letter = list(x for x in range(1, m + 1))
    # print(potential_letter)
    # chosen_letter = sample(potential_letter, n)
    # chosen_letter.sort()

    combinations = list(itertools.combinations(chosen_letter, k))

    validation_sets = []
    tmp_sets = list(itertools.combinations(chosen_letter, j))
    # tmp_sets = list(combine(chosen_letter, 10, 6, 5))
    if j == s:
        result = select(len(chosen_letter), combinations, tmp_sets)
    else:
        tmp_sets_index = 0
        while tmp_sets_index < len(tmp_sets):
            tmp_set = tmp_sets[tmp_sets_index]
            # jCs
            small = list((itertools.combinations(tmp_set, s)))
            # 找出这一组tmp_set（nCj）中哪一组（jCs）同样会被剩余的nCj覆盖，被覆盖最多的jCs记为d
            d = statistic_reverse(tmp_sets, small)
            validation_sets.append(d)
        validation_sets = remove_duplicate_rows(validation_sets)
        result = select(len(chosen_letter), combinations, validation_sets)


    return result


if __name__ == '__main__':
    time1 = time.time()
    search(45, 16, 6, 4, 4)
    time2 = time.time()
    print(time2 - time1)

