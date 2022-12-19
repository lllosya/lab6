import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csvfile) -> list[dict]:
    json_array = []
    with open(csvfile) as csvf:
        i = 0
        for line in csvf:
            if i == 0:
                i += 1
                header = line
            else:
                head = header.replace('\n', '').split(',')
                item = line.replace('\n', '').split(',')
                row = dict(zip(head, item))
                json_array.append(row)
    return json_array


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
