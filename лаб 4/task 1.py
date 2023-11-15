# TODO решите задачу
import json
filename = "input.json"

def task() -> float:
    with open(filename) as f:
        json_data = json.load(f)
    sum_values = sum([items["score"] + items["weight"] for items in json_data])
    return round(sum_values, 3)


print(task())
