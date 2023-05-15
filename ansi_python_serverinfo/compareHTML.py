import difflib

def compare_html_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    diff = difflib.HtmlDiff()
    diff_html = diff.make_file(lines1, lines2)

    with open(output_file, 'w') as f_out:
        f_out.write(diff_html)