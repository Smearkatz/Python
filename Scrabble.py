# https://www.codewars.com/kata/highest-scoring-word/train/python
import string


def high(x):
    my_list = []
    z = []
    score_card = {}
    for number, letter in enumerate(string.ascii_lowercase):
        score_card[letter] = number + 1

    for i in x.split():
        z.append(i)
        score = 0
        for j in i:
            score += score_card.get(j)

        my_list.append(score)

    for i in my_list:
        if i == max(my_list):
            indx = my_list.index(i)
            break
    return str(z[indx])
