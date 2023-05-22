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

    # Iterate over the headers and highlight changed column values
    for i, header in enumerate(headers):
        col_values = [row.find_all('td')[i].text.strip() for row in rows[1:]]
        unique_values = list(set(col_values))
        
        if len(unique_values) > 1:
            # If there are multiple unique values in the column, highlight the cells
            for row in rows[1:]:
                cell = row.find_all('td')[i]
                cell_value = cell.text.strip()
                if cell_value != unique_values[0]:
                    cell['style'] = 'color: red;'

    # Write the modified HTML to a new file
    new_html_file = 'modified.html'
    with open(new_html_file, 'w') as f:
        f.write(str(soup))

    print(f"Modified HTML file generated: {new_html_file}")


# Example usage
html_file = 'merged_data.html'
highlight_changed_values(html_file)
