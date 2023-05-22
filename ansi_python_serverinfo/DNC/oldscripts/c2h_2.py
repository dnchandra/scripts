import json

# Read the JSON files
with open('json/serverinfo_curr.json', 'r') as file1:
    json_data1 = json.load(file1)

with open('json/serverinfo_prev.json', 'r') as file2:
    json_data2 = json.load(file2)

# Generate the HTML page
html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Comparison Results</title>
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
    }

    th, td {
      text-align: left;
      padding: 8px;
    }

    th {
      background-color: #f2f2f2;
    }

    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>Comparison Results</h1>
'''

# Iterate over the JSON data and add tables to the HTML page
for index, json_data in enumerate([json_data1, json_data2], start=1):
    html += f'<h2>JSON File {index}</h2>'
    html += '<table>'
    # Extract the keys from the first item in the list
    keys = list(json_data[0].keys())
    # Add the table headers
    html += '<tr>'
    for key in keys:
        html += f'<th>{key}</th>'
    html += '</tr>'
    # Add the table rows
    for item in json_data:
        html += '<tr>'
        for key in keys:
            html += f'<td>{item[key]}</td>'
        html += '</tr>'
    html += '</table>'

# Complete the HTML page
html += '''
</body>
</html>
'''

# Write the HTML page to a file
with open('output.html', 'w') as output_file:
    output_file.write(html)

print("HTML page generated successfully!")
