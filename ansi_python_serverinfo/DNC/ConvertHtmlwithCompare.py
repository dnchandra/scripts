from bs4 import BeautifulSoup

def highlight_changed_values(html_file):
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

    # Create a dictionary to store unique column values for each hostname
    unique_values = {}

    # Iterate over the rows and collect unique values for each hostname
    for row in rows[1:]:
        hostname = row.find_all('td')[hostname_index].text.strip()

        if hostname not in unique_values:
            unique_values[hostname] = [row.find_all('td')[i].text.strip() for i in range(len(headers))]

        # Compare the current row's column values with the stored unique values for the hostname
        current_values = [row.find_all('td')[i].text.strip() for i in range(len(headers))]
        stored_values = unique_values[hostname]

        for i, (current_value, stored_value) in enumerate(zip(current_values, stored_values)):
            if headers[i] not in ['Uptime', 'Date'] and current_value != stored_value:
                # If the value is different and not Uptime or Date, highlight the cell
                cell = row.find_all('td')[i]
                cell['style'] = 'color: red;text-align: center;'

    # Write the modified HTML to a new file
    new_html_file = 'final.html'
    with open(new_html_file, 'w') as f:
        f.write(str(soup))

    print(f"Modified HTML file generated: {new_html_file}")


# Example usage
html_file = 'index.html'
highlight_changed_values(html_file)
