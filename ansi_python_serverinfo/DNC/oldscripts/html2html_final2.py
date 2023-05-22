from bs4 import BeautifulSoup

def merge_hostnames(html_file):
    # Read the HTML file
    with open(html_file, 'r') as f:
        html_data = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find the table element
    table = soup.find('table')
    if table is None:
        print("Error: No table found in the HTML file.")
        return

    # Get the table headers
    headers = [th.text.strip() for th in table.find_all('th')]

    # Find all the table rows
    rows = table.find_all('tr')
    if len(rows) < 2:
        print("Error: Insufficient data rows in the HTML file.")
        return

    # Find the index of the Hostname column
    hostname_index = headers.index('Hostname')

    # Create a dictionary to store merged rows for each hostname
    merged_rows = {}

    # Iterate over the rows and merge data for each hostname
    for row in rows[1:]:
        tds = row.find_all('td')
        hostname = tds[hostname_index].text.strip()

        if hostname not in merged_rows:
            merged_rows[hostname] = [tds]
        else:
            merged_rows[hostname].append(tds)

    # Generate the modified HTML
    modified_html = '<table>\n<tr>\n'
    modified_html += '\n'.join([f'<th>{header}</th>' for header in headers])
    modified_html += '</tr>\n'

    for hostname, rows in merged_rows.items():
        num_rows = len(rows)
        modified_html += f'<tr>\n<td rowspan="{num_rows}" style="text-align: center;">{hostname}</td>\n'
        modified_html += '\n'.join([''.join([f'<td>{td.text.strip()}</td>' for td in row]) for row in rows])
        modified_html += '</tr>\n'

    modified_html += '</table>'

    # Write the modified HTML to a new file
    new_html_file = 'modified.html'
    with open(new_html_file, 'w') as f:
        f.write(modified_html)

    print(f"Modified HTML file generated: {new_html_file}")


# Example usage
html_file = 'index.html'
merge_hostnames(html_file)
