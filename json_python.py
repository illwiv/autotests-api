import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)

print(parsed_data)

data = json.dumps(parsed_data, indent=4)

print(data)

with open("json_example.json", "r") as file:
    read_data = json.load(file)
    print(read_data)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(parsed_data, file, indent=2, ensure_ascii=False)
