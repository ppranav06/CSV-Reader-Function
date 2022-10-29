# CSV with default delimeter (,)

import csv
# opening a csv file with read mode
with open ("Python/CSV Reader Function/CSV/csv-without-spaces.csv", 'r') as f:
    reader = csv.reader(f)

    # print each line row by row
    for row in reader:
        print(row)

f.close()