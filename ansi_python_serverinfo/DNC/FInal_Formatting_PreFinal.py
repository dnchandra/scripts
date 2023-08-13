from bs4 import BeautifulSoup
import re

def parse_uptime(uptime):
    total_minutes = 0
    
    # Regular expression patterns to match different uptime formats
    patterns = [
        r'up\s*(\d+)\s*days,\s*(\d+)\s*hours,\s*(\d+)\s*minutes',
        r'up\s*(\d+)\s*days,\s*(\d+)\s*hours',
        r'up\s*(\d+)\s*hours,\s*(\d+)\s*minutes',
        r'up\s*(\d+)\s*hours',
        r'up\s*(\d+)\s*minutes'
    ]
    
    for pattern in patterns:
        match = re.match(pattern, uptime)
        if match:
            groups = match.groups()
            if len(groups) >= 1:
                if 'days' in uptime:
                    total_minutes += int(groups[0]) * 24 * 60
                elif 'hours' in uptime:
                    total_minutes += int(groups[0]) * 60
                else:
                    total_minutes += int(groups[0])
            if len(groups) >= 2:
                total_minutes += int(groups[1])
            if len(groups) >= 3:
                total_minutes += int(groups[2])
            break
    
    return total_minutes

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

    # Find the index of the Hostname, Kernel, Date, and Uptime columns
    hostname_index = headers.index('Hostname')
    kernel_index = headers.index('Kernel')
    date_index = headers.index('Date')
    uptime_index = headers.index('Uptime')

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
            if headers[i] == 'Kernel':
                if current_value != stored_value:
                    # If the Kernel value is different, highlight the cell in green
                    cell = row.find_all('td')[i]
                    cell['style'] = 'color: green; text-align: center;'
            elif headers[i] == 'Uptime':
                current_uptime = parse_uptime(current_value)
                if current_uptime > 30 * 24 * 60:  # More than 30 days in minutes
                    # If the uptime is greater than 30 days, highlight the cell in red
                    cell = row.find_all('td')[i]
                    cell['style'] = 'color: red; text-align: center;'
            elif headers[i] != 'Date':
                if current_value != stored_value:
                    # If any other value is different, highlight the cell in red
                    cell = row.find_all('td')[i]
                    cell['style'] = 'color: red; text-align: center;'

    # Write the modified HTML to a new file
    new_html_file = 'final1.html'
    with open(new_html_file, 'w') as f:
        f.write(str(soup))

    print(f"Modified HTML file generated: {new_html_file}")

# Example usage
html_file = 'final.html'
highlight_changed_values(html_file)
