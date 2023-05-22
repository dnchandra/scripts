import json

def convert_dict_to_list(file_path):
    # Read the file and load the data
    with open(file_path, 'r') as file:
        data = json.load(file)
    result = list(data.values())

    return result

# Specify the path to the file
file_path = "json/serverinfo.json"  # Replace with the actual path to your file

# Convert the dictionary values to a list
converted_list = convert_dict_to_list(file_path)

# Print the result
print(converted_list)


