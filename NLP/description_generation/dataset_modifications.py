import csv


aList = []

with open('descriptions.csv') as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        for element in row:
            element = element.replace('"', '').replace('\'', '').replace('..', '').strip()
            aList.append(element)

print(aList)

with open('descriptions_new.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(aList)


