# Python program to convert text
# file to JSON
import json
import glob

# the file to be converted to
# json format
#filename = 'reports/final.txt'

prevlistOffiles = glob.glob('prev_reports/*.txt')
currlistoffiles = glob.glob('curr_reports/*.txt')

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
out_file = open("json/serverinfo.json", "w")
out_file.write("[")
i = 0;
for file in prevlistOffiles:
    i += 1;
    with open(file) as fh:
        for line in fh:

        # reads each line and trims of extra the spaces
        # and gives only the valid words
            command, description = line.strip().split(':',1)
            dict1[command] = description.strip()
            print(dict1[command])
           # print(line)
    out_file = open("json/serverinfo.json", "a")
    print(file)
    if i > 1:
        out_file.writelines(',')
    json.dump(dict1, out_file, indent = 4, sort_keys = False)
    #out_file = open("json/serverinfo.json", "a")
    #out_file.write(",")
    #out_file.close()

# creating json file
# the JSON file is named as test1
#out_file = open("json/serverinfo.json", "a")
#json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file = open("json/serverinfo.json", "a")
out_file.write("]")
print("JSON created successfully")
print("Processed JSON for "+str(i)+" servers")
out_file.close()
