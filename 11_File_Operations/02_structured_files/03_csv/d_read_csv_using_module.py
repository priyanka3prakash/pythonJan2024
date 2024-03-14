"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv



with open("my_file.csv", mode="r") as fh:
    # file_content = csv.reader(fh, delimiter=',')
    file_content = csv.DictReader(fh, delimiter=',')
    print(file_content, type(file_content))

    names = []
    for each_line_dict in file_content:
        # print('each_line_dict', each_line_dict)
        name = each_line_dict['name']
        names.append(name)

print(f'{names = }')