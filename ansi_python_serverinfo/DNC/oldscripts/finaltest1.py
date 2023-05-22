from bs4 import BeautifulSoup


def merge_rows(html_file):
    # Load HTML file
    with open(html_file, 'r') as file:
        html_data = file.read()

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_data, 'html.parser')
    table = soup.find('table')

    # Create a dictionary to store merged rows
    merged_rows = {}

    # Iterate over table rows
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 0:
            key = columns[0].text.strip()
            if key not in merged_rows:
                # Store the first occurrence of the key
                merged_rows[key] = [columns]
            else:
                # Add the current row to the existing rows with the same key
                merged_rows[key].append(columns)

    # Replace the table rows with merged rows
    table.clear()
    for key in merged_rows:
        rows_with_same_key = merged_rows[key]
        for i, row_columns in enumerate(rows_with_same_key):
            new_row = soup.new_tag('tr')
            if i == 0:
                # Merge the first column for the first row with the same key
                first_column = soup.new_tag('td', rowspan=len(rows_with_same_key))
                first_column.string = key
                new_row.append(first_column)
            for column in row_columns:
                new_row.append(column)
            table.append(new_row)

    # Save the modified HTML to a new file
    new_html_file = html_file.replace('.html', '_merged.html')
    with open(new_html_file, 'w') as file:
        file.write(str(soup))


# Test the function
html_file = 'final1.html'
merge_rows(html_file)
print(f"HTML file with merged rows generated: {html_file.replace('.html', '_merged.html')}")
