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
                merged_rows[key] = columns
            else:
                # Merge the current row with the existing row
                existing_columns = merged_rows[key]
                for i, column in enumerate(columns):
                    if i > 0:
                        existing_columns[i].extract()
                        existing_columns[i].append(column.text.strip())

    # Replace the table rows with merged rows
    table.clear()
    for key in merged_rows:
        merged_row = merged_rows[key]
        new_row = soup.new_tag('tr')
        for column in merged_row:
            new_row.append(column)
        table.append(new_row)

    # Save the modified HTML to a new file
    new_html_file = html_file.replace('.html', '_merged.html')
    with open(new_html_file, 'w') as file:
        file.write(str(soup))


# Test the function
html_file = 'index.html'
merge_rows(html_file)
print(f"HTML file with merged rows generated: {html_file.replace('.html', '_merged.html')}")
