import json

# Read the JSON files
with open('json/serverinfo_curr.json', 'r') as file1:
    json_data1 = json.load(file1)

with open('json/serverinfo_prev.json', 'r') as file2:
    json_data2 = json.load(file2)

# Compare the "Hostname" key value
hostnames1 = [data['Hostname'] for data in json_data1]
hostnames2 = [data['Hostname'] for data in json_data2]

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
  <table>
    <tr>
      <th>Hostname</th>
      <th>JSON File 1</th>
      <th>JSON File 2</th>
    </tr>
'''

# Iterate over hostnames and add rows to the HTML table
for hostname in hostnames1:
    row = f'''
    <tr>
      <td>{hostname}</td>
      <td>{json_data1[hostnames1.index(hostname)]}</td>
      <td>{json_data2[hostnames2.index(hostname)]}</td>
    </tr>
    '''
    html += row

# Complete the HTML page
html += '''
  </table>
</body>
</html>
'''

# Write the HTML page to a file
with open('comparison_results.html', 'w') as output_file:
    output_file.write(html)

print("HTML page generated successfully!")
