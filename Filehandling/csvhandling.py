import csv

with open("/dataformats/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("/dataformats/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "marks"])
    writer.writerow([1, "Rahul", 85])
    writer.writerow([2, "Anita", 90])

with open("/dataformats/data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Kiran", 88])