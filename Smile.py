def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    count = 0

    for i in arr:
        if len(i) == 3:
            if i[0] in eyes and i[1] in nose and i[2] in mouth:
                count += 1

        elif len(i) == 2:
            if i[0] in eyes and i[1] in mouth:
                count += 1
    return count



print(count_smileys(([':D',':~)',';~D',':)'])))