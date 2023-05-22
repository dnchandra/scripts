import json

# Read the contents of the first JSON file
with open('json/serverinfo_prev.json', 'r') as file1:
    json_data1 = json.load(file1)

# Read the contents of the second JSON file
with open('json/serverinfo_curr.json', 'r') as file2:
    json_data2 = json.load(file2)

# Merge the dictionaries
merged_data = json_data1 + json_data2

# Sort the merged list of dictionaries based on a specific key (e.g., 'name')
sorted_data = sorted(merged_data, key=lambda x: x['Hostname'])

# Generate a new JSON file with the sorted data
with open('json/serverinfo.json', 'w') as output_file:
    json.dump(sorted_data, output_file)

# Print the data on the terminal
for item in sorted_data:
    print(item)
