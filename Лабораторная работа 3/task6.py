list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = {"index": 0, "value" : list_numbers[0]}
for index, num in enumerate(list_numbers):
    if num > max_number["value"]:
        max_number["index"] = index
        max_number["value"] = num

temp = list_numbers[-1]
list_numbers[-1] = list_numbers[max_number["index"]]
list_numbers[max_number["index"]] = temp
print(list_numbers)

