# CSV with custom delimeter (here: |)

import csv

csv.register_dialect('myDialect', delimiter='|', skipinitialspace=True)

f = open("Python/CSV Reader Function/CSV/csv-custom-delimiter.csv",'r')
reader = csv.reader(f, dialect="myDialect")

# print each line row by row
for row in reader:
    print(row)

f.close()