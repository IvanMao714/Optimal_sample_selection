import itertools
from random import sample
from random import choice
from utils import stack
import numpy as np

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


def select(combinations, validation_sets):
    print(f"===========================Select Function===============================")
    valid_combinations = []
    print("-----------validation_sets----------")
    print(validation_sets)
    print(len(validation_sets))
    # combinations.reverse()
    print("--------combinations----")

    # combinations_r = list(reversed(combinations))
    # print("combinations:" + str(combinations))
    # combinations.reverse()
    # combinations_r = list(reversed(combinations))
    # combinations.sort()
    # while(len(validation_sets) != 0):

    while (len(validation_sets) != 0):
        combination = satistic(combinations, validation_sets)
        print("combination:" + str(combination))
        # for combination in combinations:
        # for combination in combinations:
        # flag = 0
        # print("combination:" + str(combination))
        # if len(validation_sets) == 0:
        #     break
        for validation_set in validation_sets:
            print("validation_set:" + str(validation_set))
            if set(validation_set).issubset(set(combination)):
                print("-------------------------")
                flag = 1

        validation_sets = [s for s in validation_sets if not set(s).issubset(set(combination))]
        if flag == 1:
            valid_combinations.append(combination)
            print("^^^^^^^^^^^^")
            print("Add combination" + str(combination))
            # break
            # print("++++++++++++++++++++++++++++++++++")
            # print(valid_combinations)
        print("num of validation_sets:" + str(len(validation_sets)))
        print("num of valid_combinations:" + str(len(valid_combinations)))
    print("---------------------result--------------------------")
    print(valid_combinations)
    print(len(valid_combinations))
    return valid_combinations

def remove_duplicate_rows(arr):
    unique_rows = []
    seen = set()

    for row in arr:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(list(row_tuple))

    return unique_rows
def satistic(combinations, validation_sets):
    max_count = 0
    max_list = []
    combinations.reverse()
    print("combinations_r:" + str(combinations))
    for combination in combinations:
        count = 0
        # for combination in combinations:
        for validation_set in validation_sets:
            if set(validation_set).issubset(set(combination)):
                # print("-------------------------")
                count += 1
        if count > max_count:
            max_count = count
            max_list = combination
        # weight.update({combination: count})
        print("combination:" + str(combination) + ",count:"+str(count))

    # weight = sorted(weight, key=lambda x:x[0])
    combinations.remove(max_list)
    print("weight:" + str(max_count))
    return max_list


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H", 'I', "J", 'K', 'L']  # test
    # choosen_letter = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(choosen_letter)

    combinations = list(itertools.combinations(choosen_letter, k))
    print("combinations" + str(combinations))
    print("lens:" + str(len(combinations)))

    validation_sets = []
    validation_sets = list(itertools.combinations(choosen_letter, j))
    validation_sets = select(combinations, validation_sets)
    print("final_validation_sets:" + str(validation_sets))
    print("length:" + str(len(validation_sets)))
    # combinations = combine(choosen_letter, n, k, s)

    # select(combinations, validation_sets)

# def sso(m, n, k, j, s):



if __name__ == '__main__':
    # search(45, 10, 6, 6, 4)
    #search(45, 9, 6, 4, 4)
    search(45, 12, 6, 6, 4)