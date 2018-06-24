# https://www.codewars.com/kata/directions-reduction/train/python
def dirReduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    way = []
    for i in arr:
        if way:
            if opposite[i] == way[-1]:
                way.pop()
            else:
                way.append(i)
        else:
            way.append(i)
    return way



print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))