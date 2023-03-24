import itertools
from random import sample


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H"] # test
    print(choosen_letter)
    combination = []
    for x in range(n-k+1):
        print(f"======the "+ str(x) + "th========" )
        head_letters = choosen_letter[n-k-x:n-k+s-x]
        tail_letters = choosen_letter[n-k+s-x:]
        print(head_letters, tail_letters)
        # first_combination = choosen_letter[-6:]
        # print(first_combination)

        if len(tail_letters) != 0:
            tail_combinations = list(itertools.combinations(tail_letters, k-s))
        print(tail_combinations)


if __name__ == '__main__':
    search(45, 8, 6, 4, 4)
    # search(45, 7, 6, 5, 5)
