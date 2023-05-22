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
dict2 = {}
# creating dictionary
out_file = open("json/serverinfo_curr.json", "w")
out_file1 = open("json/serverinfo_prev.json", "w")
out_file.write("[")
out_file1.write("[")

i = 0;
for file in currlistoffiles:
    i += 1;
    with open(file) as fh:
        for line in fh:

        # reads each line and trims of extra the spaces
        # and gives only the valid words
            command, description = line.strip().split(':',1)
            dict1[command] = description.strip()
            print(dict1[command])
           # print(line)
    out_file = open("json/serverinfo_curr.json", "a")
    print(file)
    if i > 1:
        out_file.writelines(',')
    json.dump(dict1, out_file, indent = 4, sort_keys = False)


j = 0
for file in prevlistOffiles:
    j += 1;
    with open(file) as fh:
        for line in fh:

        # reads each line and trims of extra the spaces
        # and gives only the valid words
            command, description = line.strip().split(':',1)
            dict2[command] = description.strip()
            print(dict2[command])
           # print(line)
    out_file1 = open("json/serverinfo_prev.json", "a")
    print(file)
    if j > 1:
        out_file1.writelines(',')
    json.dump(dict2, out_file1, indent = 4, sort_keys = False)


out_file1 = open("json/serverinfo_prev.json", "a")
out_file1.write("]")

out_file1.close()
out_file = open("json/serverinfo_curr.json", "a")
out_file.write("]")
out_file.close()
