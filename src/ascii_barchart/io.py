import csv

def load_rows(csv_path):
    row_list = []
    with open(csv_path) as f:
        for row in csv.reader(f):
            row_list.append(row)
    row_list.pop(0)
    return row_list