import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data, indent=4)
print(json_string)
