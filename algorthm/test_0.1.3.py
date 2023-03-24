import itertools
from random import sample


def combine(choosen_letter, n, k,s):
    combination = []
    for x in range(n-k+1):
        print(f"======the " + str(x) + "th========")
        head_letters = choosen_letter[n - k - x:n - k + s - 2*x]
        tail_letters = choosen_letter[n - k + s - 2*x:]
        print(head_letters, tail_letters)
        # first_combination = choosen_letter[-6:]
        # print(first_combination)

        if len(tail_letters) != 0:
            tail_combinations = list(itertools.combinations(tail_letters, x+k-s))
        for tc in tail_combinations:
            # temp = head_letters.append(tc)
            combination.append(head_letters + list(tc))
        print(combination)
    return combination


def search(m, n, k, j, s):
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H", "I"]  # test
    print(choosen_letter)

    combination = combine(choosen_letter, n, k,s)

    print("========final result===========")
    print(combination)
    print(len(combination))

if __name__ == '__main__':
    search(45, 9, 6, 4, 4)
    # search(45, 7, 6, 5, 5)
