import json

# Read the JSON files
with open('json/serverinfo_prev.json', 'r') as file1:
    json_data1 = json.load(file1)

with open('json/serverinfo_curr.json', 'r') as file2:
    json_data2 = json.load(file2)

# Generate the HTML page
html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Merged Data</title>
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
  <h1>Merged Data</h1>
  <table>
    <tr>
'''

# Add the column names from the first file to the HTML table
for key in json_data1[0].keys():
    html += f'<th>{key}</th>'

html += '</tr>'

# Add the rows from the first file to the HTML table
for item in json_data1:
    html += '<tr>'
    for value in item.values():
        html += f'<td>{value}</td>'
    html += '</tr>'

# Add the rows from the second file to the HTML table
for item in json_data2:
    html += '<tr>'
    for value in item.values():
        html += f'<td>{value}</td>'
    html += '</tr>'

# Complete the HTML page
html += '''
  </table>
</body>
</html>
'''

# Write the HTML page to a file
with open('merged_data.html', 'w') as output_file:
    output_file.write(html)

print("HTML page generated successfully!")
