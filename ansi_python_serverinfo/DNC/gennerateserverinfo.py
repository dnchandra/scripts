import json


def compare_json_files(file1_path, file2_path, output_file_path):
    # Load the contents of the first JSON file
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)
        print(list(data1[0].values()))
    # Load the contents of the second JSON file
    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)
        for x in range(len(data2)):
          print(list(data2[x].values()))
     

    # Compare the data in both files
    matched_data = []


    for item1 in data1:
       # print(item1)
        

        i = 0
        for x in item1:

            if(i == 0):
               file1_host = item1.get(x)
              # print("file 1"+item1.get(x))
               i += 1

        for item2 in data2:
               

                j = 0
                
                for y in item2:
                     if(j == 0):
                          file2_host = item2.get(y)
                          list
                       #   print("file 2"+item2.get(y))
                          j += 1
                     
                #if(file1_host==file2_host):
                 #  print("matched")
                matched_data.append(item1)
                matched_data.append(item2)
                break
                

               # if(file1_host not in item1.get(x))



    # Write the matched data to the output file
    with open(output_file_path, 'w') as output_file:
        json.dump(matched_data, output_file, indent=4)

   

# Specify the paths to the JSON files
file1_path = "json/serverinfo_curr.json"  # Replace with the actual path to the first JSON file
file2_path = "json/serverinfo_prev.json"  # Replace with the actual path to the second JSON file
output_file_path = "json/serverinfo.json"  # Replace with the desired path for the output file

# Compare the JSON files and write the matched data
compare_json_files(file1_path, file2_path, output_file_path)
