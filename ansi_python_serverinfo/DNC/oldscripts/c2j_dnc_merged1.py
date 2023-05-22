import json

# Read the contents of the first JSON file
with open('json/serverinfo_curr.json', 'r') as file1:
    data1 = json.load(file1)

# Read the contents of the second JSON file
with open('json/serverinfo_prev.json', 'r') as file2:
    data2 = json.load(file2)

# Compare the lists
common_lists = []
unique_lists_file1 = []
unique_lists_file2 = []

for list1 in data1:
    if list1 in data2:
        common_lists.append(list1)
    else:
        unique_lists_file1.append(list1)

for list2 in data2:
    if list2 not in data1:
        unique_lists_file2.append(list2)

# Print the results
print("Common lists:")
for common_list in common_lists:
    print(common_list)

print("Unique lists in file1:")
for unique_list_file1 in unique_lists_file1:
    print(unique_list_file1)

print("Unique lists in file2:")
for unique_list_file2 in unique_lists_file2:
    print(unique_list_file2)

with open('json/common_lists.json', 'w') as common_file:
    json.dump(common_lists, common_file)

with open('json/unique_lists_curr.json', 'w') as unique_file1:
    json.dump(unique_lists_file1, unique_file1)

with open('json/unique_lists_prev.json', 'w') as unique_file2:
    json.dump(unique_lists_file2, unique_file2)