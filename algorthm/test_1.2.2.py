import itertools
from random import sample

from utils import stack


def combine(choosen_letter, n, k, s):
    combination = []
    head_combinations, tail_combinations=[],[]
    # for x in range(n - k + 1):
    print(f"==============")
    # head_letters = choosen_letter[:n-k+x-1]
    # head_combinations = list(itertools.combinations(head_letters, x))
    # for head_combination in head_combinations:
    # print("head_combination" + str(head_combinations))
    middle_letters = choosen_letter[:n-k+s]
    middle_combinations = list(itertools.combinations(middle_letters, s))
    tail_letters = choosen_letter[n-k+s:]
    tail_combinations = list(itertools.combinations(tail_letters, k-s))
    # print(head_letters, middle_combinations, tail_combinations)
    print(middle_combinations, tail_combinations)
    for middle_combination in middle_combinations:
        for tail_combination in tail_combinations:
            # print(list(tail_combination))
            temp = list(middle_combination) + list(tail_combination)
            print("temp"+str(temp))
            combination.append(list(middle_combination) + list(tail_combination))


        # combination.append([head_combinations+list(middle_combination)+list(tail_combination) for middle_combination in middle_combinations for tail_combination in tail_combinations ])
        # if len(head_letters) != 0:
        #     head_combinations = list(itertools.combinations(head_letters, s-x+1))
        # if len(tail_letters) != 0:
        #     tail_combinations = list(itertools.combinations(tail_letters, k - s))
        # print(list(head_combinations), list(tail_combinations))
        # for tc in tail_combinations:
        #     # temp = head_letters.append(tc)
        #     combination.append(head_letters + middle_letters + list(tc))
        # print(combination)
        # t = t+1
    print("========final combination===========")
    print(combination)
    print(len(combination))
    return combination


def select(combinations, choosen_letter, j, s):
    print("================================================select=============================")
    valid_combinations = []
    tmp_sets = sample(choosen_letter, j)
    tmp_sets.sort()
    tmp_sets = list(itertools.combinations(choosen_letter, j))
    validation_sets = tuple(itertools.combinations(tmp_sets, s))
    print("-----------validation_sets----------")
    print(validation_sets)
    print(len(validation_sets))
    # combinations.reverse()
    print("--------combinations----")

    # combinations_r = list(reversed(combinations))
    print("combinations:" + str(combinations))
    # combinations.reverse()
    # combinations_r = list(reversed(combinations))
    combinations.sort()
    print("combinations_r:"+str(combinations))
    for combination in combinations:
        # for combination in combinations:
        flag = 0
        print("combination:" + str(combination))
        if len(validation_sets) == 0:
            break
        for validation_set in validation_sets:
            if set(validation_set).issubset(set(combination)):
                validation_sets = [s for s in validation_sets if not set(s).issubset(set(combination))]
                flag = 1
        if flag == 1:
            valid_combinations.append(combination)
            print("^^^^^^^^^^^^")
            print("Add combination" + str(combination))
            # break
            print("___________________")
            print(valid_combinations)
            print("num of validation_sets:" + str(len(validation_sets)))
    print("++++++++++++result+++++++++++")
    print(valid_combinations)
    print(len(valid_combinations))


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # test
    print(choosen_letter)

    combinations = combine(choosen_letter, n, k, s)

    # select(combinations, choosen_letter, j, s)


if __name__ == '__main__':
    # search(45, 10, 6, 6, 4)
    search(45, 8, 6, 4, 4)
