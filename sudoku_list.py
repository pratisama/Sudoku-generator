import random, time

start_time = time.perf_counter


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
list_input = list(nums)
house_no = 4

for i in range(0, 9):
    row_no = i + 1

    if i in (3, 6):
        house_no = row_no
    else:
        house_no = house_no - 3

    for j in range(9):
        column_no = j + 1

        while True:
            inserstion = list_input[random.randint(0, len(list_input) - 1)]
            if (
                inserstion not in row_dict[row_no]
                and inserstion not in column_dict[column_no]
                and inserstion not in house_dict[house_no]
            ):
                break
            else:
                continue

        row_dict[row_no].append(inserstion)
        column_dict[column_no].append(inserstion)
        house_dict[house_no].append(inserstion)

        if len(row_dict[row_no]) % 3 == 0:
            house_no += 1

end_time = time.perf_counter
out(row_dict)
print()
out(column_dict)
print()
out(house_dict)
print(f"\ntime taken: {(end_time-start_time):.4f} secs")  # type: ignore
