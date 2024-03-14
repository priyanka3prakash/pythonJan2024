"""
Purpose: Reading(Parsing) CSV using csv module
"""
import csv


# print(dir(csv))

# for each_attribute in dir(csv):
#     if each_attribute.startswith('__'):
#         continue
#     print(each_attribute)


with open("my_file.csv", mode="r") as fh:
    # file_content = fh.read()

    file_content = csv.reader(fh, delimiter=',')
    print(file_content, type(file_content))
    # print(list(file_content))

    # To skip a row
    next(file_content)
    
    names = []
    for each_line_list in file_content: # [1:]:
        # print('each_line_list', each_line_list)
        name = each_line_list[1]
        names.append(name)

print(f'{names = }')