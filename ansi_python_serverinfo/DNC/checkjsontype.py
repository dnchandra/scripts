import json

def check_json_type(file_path):
    # Read the file and load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)
        #return data
        print(data[0])
    # Check the type of the loaded data
    if isinstance(data, dict):
        return "dictionary"
    elif isinstance(data, list):
        return "list"
    else:
        return "other"
    
# Specify the path to the JSON file
file_path = "json/serverinfo.json"  # Replace with the actual path to your JSON file

# Check the type of the JSON file
json_type = check_json_type(file_path)

# Print the result
print("The JSON file represents:", json_type)

