import random


def out(dict: dict):
    for i in range(len(dict)):
        print(dict[i + 1])


row_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}
column_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}
house_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
list_pop = []
house_no = 4

for i in range(9):

    if i in (3, 6):
        house_no = i + 1
    else:
        house_no = house_no - 3

    list_input = list(nums)
    for j in range(9):
        popped = list_input.pop(random.randint(0, len(list_input) - 1))
        row_dict[i + 1].append(popped)
        column_dict[j + 1].append(popped)
        house_dict[house_no].append(popped)

        if len(row_dict[i + 1]) % 3 == 0:
            house_no += 1

out(row_dict)
print()
out(column_dict)
print()
out(house_dict)
