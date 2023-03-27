import itertools
from random import sample

from utils import stack


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


def select(combinations, choosen_letter, j, s):
    print(f"===========================Select Function===============================")
    valid_combinations = []
    validation_sets = []
    # tmp_sets = sample(choosen_letter, j)
    # tmp_sets.sort()
    # tmp_sets = itertools.combinations(choosen_letter, s)
    validation_sets = list(itertools.combinations(choosen_letter, s))
    # print(tmp_sets)
    # print(len(tmp_sets))
    # for tmp_set in tmp_sets:
    #     # print(itertools.combinations(tmp_set, s))
    #     validation_sets = validation_sets + list(itertools.combinations(tmp_set, s))
    #     # validation_sets = tuple(itertools.combinations(tmp_sets, s))
    #     # print(validation_sets)

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
    print("combinations_r:" + str(combinations))
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
    # print("---------------------result--------------------------")
    # print(valid_combinations)
    # print(len(valid_combinations))


def satistic(combinations, validation_sets):
    max_count = 0
    max_list = []
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

    # weight = sorted(weight, key=lambda x:x[0])
    print("weight:" + str(max_count))
    return max_list


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H"]  # test
    print(choosen_letter)

    combinations = combine(choosen_letter, n, k, s)

    select(combinations, choosen_letter, j, s)


if __name__ == '__main__':
    # search(45, 10, 6, 6, 4)
    search(45, 8, 6, 4, 4)
