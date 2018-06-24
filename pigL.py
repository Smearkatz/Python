# https://www.codewars.com/kata/simple-pig-latin/train/python
def pig_it(text):
    new = []
    if text == ():
        return ()
    else:
        for word in text.split():
            first = word[0]
            if first.isalpha():
                new.append(word[1:] + first + 'ay')
            else:
                new.append(word[1:] + first)
        return ' '.join(new)


print(pig_it('Pig latin is cool !'))