# CSV with spaces at the beginning

import csv

# Registering a dialect (myDialect) which defines delimeter and initial space
csv.register_dialect("myDialect", delimiter=',', skipinitialspace=True)

# opening a csv file with read mode
f = open ("Python/CSV Reader Function/CSV/csv-with-spaces.csv", 'r')
reader = csv.reader(f, dialect="myDialect")

# print each line row by row
for row in reader:
    print(row)

f.close()