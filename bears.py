# https://www.codewars.com/kata/offspring-traits/train/python
def bear_fur(bears):
    x = bears[0]
    y = bears[1]
    real = ['black', 'brown', 'white']
    if bears:
        for i in bears:
            if i not in real:
                return 'unknown'
            elif x == y:
                return x
            elif x  == 'black' or y == 'black':
                if y == 'brown' or x == 'brown':
                    return 'dark brown'
                elif y == 'white' or x == 'white':
                    return 'grey'
            elif x == 'brown' or y == 'brown':
                if y == 'white' or x == 'white':
