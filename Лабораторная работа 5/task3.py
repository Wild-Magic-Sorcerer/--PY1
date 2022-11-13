import random


def get_unique_list_numbers() -> list[int]:
    lis = []
    while len(lis) != 15:
        if (val := random.randint(-10, 10)) in lis:
            continue
        else:
            lis.append(val)
    return lis


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

