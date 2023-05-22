import json
from datetime import datetime

with open('json/serverinfo.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    # Creating an HTML file
    Func = open("index.html","w")
    htmlStr = "<html>\n<head>\n<title> \nJSON to HTML \n\
           </title>\n</head> <body bgcolor='#2D2B32'><h1 align='center' style='color:#1274B8'>Server Information</u></h1>\n<h3 align='center' style='color:#1274B8'>Report Date: "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"</h3>\
           \n<table width = '100%' border='1'>\n"
    #print(fcc_data[0]['id'])
    htmlStr += "\n<thead style='color: #fff; background: #1274B8;'><tr>"
    for key in fcc_data[0]:
        htmlStr += "<th>"+key.title()+"</th>"
    htmlStr += "\n</thead></tr>"
    
        #break
    for value in fcc_data:
        htmlStr += "\n<tr>"
        for rows in value:
            htmlStr += "\n<td style='text-align: center;color:white'>"+value[rows]+"</td>"
            print(value[rows])   
        htmlStr += "\n</tr>"
    htmlStr += "\n</table>\n</body>\n</html>"
# Adding input data to the HTML file
Func.write(htmlStr)
              
# Saving the data into the HTML file
Func.close()
