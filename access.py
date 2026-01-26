import csv

with open('cars.csv', newline='') as csvfile:
    reader = csv.DictWriter(csvfile)
    cars = list(reader)
    fieldnames = reader.fieldnames

cars[1]['Price'] = '4500.00'

with open('cars.csv','w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cars)
