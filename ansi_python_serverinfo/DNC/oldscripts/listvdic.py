import json

def convert_list_to_dict(file_path):
    # Read the file and load the data as a list
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Convert the list to a dictionary
    result = {index: value for index, value in enumerate(data)}

    return result


# Specify the path to the file
file_path = "json/serverinfo.json"  # Replace with the actual path to your file

# Convert list values to a dictionary
dict_result = convert_list_to_dict(file_path)
print("List to Dictionary:")
print(dict_result)
print(dict_result.keys())
#print(type(dict_result))
#print(dict_result.values())

