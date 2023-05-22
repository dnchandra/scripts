import json

# Read the contents of the first JSON file
with open('json/serverinfo_curr.json', 'r') as file1:
    data1 = json.load(file1)

# Read the contents of the second JSON file
with open('json/serverinfo_prev.json', 'r') as file2:
    data2 = json.load(file2)

# Extract the Hostname values from each file
hostnames1 = [item.get('Hostname') for item in data1]
hostnames2 = [item.get('Hostname') for item in data2]

# Find the common Hostname values
common_hostnames = set(hostnames1) & set(hostnames2)

# Generate the common list
common_list = [item for item in data1 if item.get('Hostname') in common_hostnames]

# Generate the missing in common list for file1
missing_in_common_file1 = [item for item in data1 if item.get('Hostname') not in common_hostnames]

# Generate the missing in common list for file2
missing_in_common_file2 = [item for item in data2 if item.get('Hostname') not in common_hostnames]

# Write the common list to a JSON file
with open('common_list.json', 'w') as common_file:
    json.dump(common_list, common_file)

# Write the missing in common list for file1 to a JSON file
with open('missing_in_common_file1.json', 'w') as missing_file1:
    json.dump(missing_in_common_file1, missing_file1)

# Write the missing in common list for file2 to a JSON file
with open('missing_in_common_file2.json', 'w') as missing_file2:
    json.dump(missing_in_common_file2, missing_file2)
# Print the common list
print("Common List:")
for item in common_list:
    print(json.dumps(item))
print()

# Print the missing items in File 1
print("Missing in File 1:")
for item in missing_in_common_file1:
    print(json.dumps(item))
print()

# Print the missing items in File 2
print("Missing in File 2:")
for item in missing_in_common_file2:
    print(json.dumps(item))