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
    kernel_index = headers.index('Kernel')

    # Create a dictionary to store previous values for each hostname
    previous_values = {}

    # Iterate over the rows and compare values
    for row in rows[1:]:
        hostname = row.find_all('td')[hostname_index].text.strip()

        if hostname not in previous_values:
            previous_values[hostname] = {}

        for i, cell in enumerate(row.find_all('td')):
            if i == kernel_index:
                # Compare Kernel values
                current_kernel = cell.text.strip()

                if 'Kernel' in previous_values[hostname]:
                    previous_kernel = previous_values[hostname]['Kernel']

                    if current_kernel != previous_kernel:
                        # If the current Kernel value is different from the previous value, highlight in green
                        cell['style'] = 'color: green; text-align: center;'
                    else:
                        # If the current Kernel value is the same as the previous value, highlight in red
                        cell['style'] = 'color: red; text-align: center;'

                previous_values[hostname]['Kernel'] = current_kernel
            elif headers[i] not in ['Uptime', 'Date']:
                # Compare other columns (except "Uptime" and "Date")
                current_value = cell.text.strip()

                if headers[i] in previous_values[hostname]:
                    previous_value = previous_values[hostname][headers[i]]

                    if current_value != previous_value:
                        # If the current value is different from the previous value, highlight in red
                        cell['style'] = 'color: red; text-align: center;'

                previous_values[hostname][headers[i]] = current_value

    # Write the modified HTML to a new file
    new_html_file = 'final1.html'
    with open(new_html_file, 'w') as f:
        f.write(str(soup))

    print(f"Modified HTML file generated: {new_html_file}")


# Example usage
html_file = 'index.html'
highlight_changed_values(html_file)
