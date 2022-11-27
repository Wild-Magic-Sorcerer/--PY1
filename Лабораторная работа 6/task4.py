import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename: str, delimiter: str = ',', new_line: str = '\n') -> list[dict]:
    with open(filename, 'r') as file:
        data = file.readlines()
        result = []
        for minidata in data[1:]:
            info = {}
            for i, j in zip(data[0].split(delimiter), minidata.split(delimiter)):
                info[i.split(new_line)[0]] = j.split(new_line)[0]
            result.append(info)
        return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

