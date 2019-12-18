import json

numbers = [2, 3, 5, 7, 11, 13, 21]

with open('json.txt','w') as file_object:
    json.dump(numbers,file_object)


with open('json.txt') as f_object:
    read_data = json.load(f_object)

print(read_data)