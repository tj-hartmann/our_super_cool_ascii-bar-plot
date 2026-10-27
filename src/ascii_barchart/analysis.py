import os
import csv

path = r"our_super_cool_ascii-bar-plot\data\points.csv"



def load_rows(csv_path):
    row_list = []
    with open(csv_path) as f:
        for row in csv.reader(f):
            row_list.append(row)
    row_list.pop(0)
    return row_list

test = load_rows(path)


def average_value1_by_type(rows):
    a_count = 0
    a = 0
    b_count = 0
    b = 0
    c_count = 0
    c = 0
    d_count = 0
    d = 0
    for row in rows:
        if row[0] == "A":
            a+= (float(row[1])) #+ float(row[2]))
            a_count += 1
        if row[0] == "B":
            b+= (float(row[1])) #+ float(row[2]))
            b_count += 1
        if row[0] == "C":
            c+= (float(row[1])) #+ float(row[2]))
            c_count += 1
        if row[0] == "B":
            d+= (float(row[1])) #+ float(row[2]))
            d_count += 1
    print(f"A {a/a_count}\n")
    print(f"B {b/b_count}\n")
    print(f"C {c/c_count}\n")
    print(f"D {d/d_count}\n")

average_value1_by_type(test)
