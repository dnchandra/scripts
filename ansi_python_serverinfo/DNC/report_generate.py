from bs4 import BeautifulSoup

def process_html(input_file):
    # Load HTML file
    with open(input_file, 'r') as file:
        html_data = file.read()

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')
    table = soup.find('table')

    # Initialize a dictionary to store the previous values for each host and column
    previous_values = {}

    # Iterate over table rows, excluding the header row
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) > 0:
            host = columns[0].get_text(strip=True)  # Hostname
            kernel = columns[5].get_text(strip=True)  # Kernel value
            deployed_lr_text = columns[9].get_text(strip=True)  # Deployed Lr Portlets value as text
            actual_lr_text = columns[10].get_text(strip=True)  # Actual Lr Portlets value as text
            uptime = columns[2].get_text(strip=True)  # Uptime value

            # Compare deployed Lr Portlets and actual Lr Portlets
            if deployed_lr_text.isdigit() and actual_lr_text.isdigit():
                deployed_lr = int(deployed_lr_text)
                actual_lr = int(actual_lr_text)
                if deployed_lr != 0 and actual_lr % deployed_lr != 0:
                    columns[10]['style'] = 'color: red; text-align: center;'  # Highlight in red and center the text

            # Compare kernel with previous value
            if host in previous_values and 5 in previous_values[host]:
                prev_kernel = previous_values[host][5]
                if prev_kernel == kernel:
                    columns[5]['style'] = 'color: red; text-align: center;'  # Highlight in red and center the text
                else:
                    columns[5]['style'] = 'color: green; text-align: center;'  # Highlight in green and center the text

            # Compare all columns from index 11 to the end with previous values
            for col_index, column in enumerate(columns[11:], start=11):
                column_text = column.get_text(strip=True)
                if host in previous_values and col_index in previous_values[host]:
                    prev_value = previous_values[host][col_index]
                    if column_text != prev_value:
                        column['style'] = 'color: red; text-align: center;'  # Highlight in red and center the text

            # Highlight Uptime column if greater than 30 days or contains "week"
            if "week" in uptime or ("days" in uptime and int(uptime.split()[0]) > 30):
                columns[2]['style'] = 'color: red; text-align: center;'  # Highlight in red and center the text

            # Update previous values for the host
            previous_values[host] = {2: uptime, 5: kernel, 9: deployed_lr_text, 10: actual_lr_text}
            for col_index, column in enumerate(columns[11:], start=11):
                previous_values[host][col_index] = column.get_text(strip=True)

    # Center all rows including header row
    for row in table.find_all('tr'):
        row['style'] = 'text-align: center;'

    # Save the modified HTML to final.html
    new_html_file = 'prefinal.html'
    with open(new_html_file, 'w') as file:
        file.write(str(soup))

    print(f"HTML file with highlighting and centered rows generated: {new_html_file}")

# Test the function with index.html
html_file = 'index.html'
process_html(html_file)
