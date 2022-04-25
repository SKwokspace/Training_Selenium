import csv

path = r"C:\Users\MohanMadhuri\PycharmProjects\My_Selenium\demo\joggers"


def read_csv():
    with open("joggers.csv") as file:
        rows = csv.DictReader(file)
        header = next(rows)
        for row in rows:
            print(rows)


print(read_csv())

