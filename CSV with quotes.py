# CSV with quotes

import csv

# Registering a dialect
csv.register_dialect('myDialect', delimiter=',', skipinitialspace=True)

# Opening file in read mode
f=open("CSVquotes.csv", 'r')
reader = csv.reader(f, dialect="myDialect", quoting=csv.QUOTE_ALL)

# print each line row by row
for row in reader:
    print(row)

f.close()

