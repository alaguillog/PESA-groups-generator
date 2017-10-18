#######################################
#RANDOM LIST GENERATOR FOR PESA GROUPS#
#######################################
#Author: Andrea Laguillo
#Input: a .csv file
#Output: a .csv file with randomnized groups

#IMPORTING NECESSARY MODULES
from random import shuffle
import csv

#ASKING FOR USER INPUT
path = input("Enter the path to your .csv file: ")
outpath = input("Enter the path where the output file will be created: ")
biggest = int(input("How many elements are in the biggest group? "))
header = str(input("Does the file have a header?(Y/N) "))
header = header.upper()
valid = 0
while valid == 0:
    if header == "Y":
        has_header = True
        valid = 1
    elif header == "N":
        has_header = False
        valid = 1
    else:
        print('Please type only "Y" or "N".')
        header = (input("Does the file have a header?(Y/N) "))

#READING DATA FROM A CSV FILE
print("Reading the file...")
list_of_lines = []
try:
    with open(path, "r") as input_file:
        input_reader = csv.reader(input_file, delimiter = ',')
        if has_header == True:
            next(input_file)
        for row in input_reader:
            list_of_lines.append(row)
except IOError:
    print("The file does not exist or could not be opened.")
    raise SystemExit
except FileNotFoundError:
    print("The file does not exist or could not be opened.")
    raise SystemExit
    
#MAKING THE GROUPS
print("Making the groups...")
case_list = []
control_list = []
for element in list_of_lines:
    if element[2] == "Caso":
        case_list.append(element)
    elif element[2] == "Control":
        control_list.append(element)
    else:
        print("Error: Unexpected input found at row ", list_of_lines.index(element) + 1, ", column 3.", sep = "")
        raise SystemExit

case_1_list = []
case_2_list = []
case_3_list = []
case_4_list = []
for i in case_list:
    if i[3] == "1":
        case_1_list.append(i[0])
    elif i[3] == "2":
        case_2_list.append(i[0])
    elif i[3] == "3":
        case_3_list.append(i[0])
    elif i[3] == "4":
        case_4_list.append(i[0])
    else:
        print("Error: Unexpected input found at row ", list_of_lines.index(i) + 1, ", column 4.", sep = "")
        raise SystemExit
shuffle(case_1_list)
shuffle(case_2_list)
shuffle(case_3_list)
shuffle(case_4_list)

mother_of_all_lists = []
for j in range(0, biggest):
    temp = []
    try:
        temp.append(case_1_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append(case_2_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append(case_3_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append(case_4_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append("C" + case_1_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append("C" + case_2_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append("C" + case_3_list[j])
    except IndexError:
        temp.append("-")
    try:
        temp.append("C" + case_4_list[j])
    except IndexError:
        temp.append("-")
    shuffle(temp)
    mother_of_all_lists.append(temp)

#WRITING THE RESULTS TO A CSV FILE
print("Writing output file...")
try:
    with open(outpath, "w") as output_file:
        output_writer = csv.writer(output_file, delimiter = ',', lineterminator = "\n")
        labels = ["","127_N","127_C","128_N","128_C","129_N","129_C","130_N","130_C"]
        output_writer.writerow(labels)
        for item in mother_of_all_lists:
            my_index = str(mother_of_all_lists.index(item) + 1)
            add = "TMT" + my_index
            item.insert(0, add)
            output_writer.writerow(item)
except IOError:
    print("The output file could not be created.")
else:
    print("Done!")
