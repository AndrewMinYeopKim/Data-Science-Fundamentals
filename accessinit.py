# first version for access.py
import csv
to_update = ['1999','Chevy','Venture']
new_price = '4500.00'
updated_rows = []
with open('cars.csv', 'r') as csvfile:
    fieldnames = "Years Make Model Price".split()
    reader = csv.DictReader(csvfile)
    for row in reader:
        if set(to_update).issubset(set(row.values())):
            row['Price'] = new_price
        updated_rows.append(row)

with open('cars.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)
