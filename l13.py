import csv


def openCsv():
    file = open("oscar_age_female.csv")
    data1 = file.read()
    file.seek(0)
    data2 = csv.reader(file)
    #print(data1)
    print(data2)
    for row in data2:
        print(row[4])
        
openCsv()

def oldest():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    oldest_age = 0
    name=""
    for row in data:
        if row[2]!="Age":
            age = int(row[2])
            if age>oldest_age:
                oldest_age=age
                name=row
    print(oldest_age)
    print(name)

def youngest():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    youngest_age = 1000
    name=""
    for row in data:
        if row[2]!="Age":
                age = int(row[2])
                if age<youngest_age:
                    youngest_age=age
                    name=row
        print(youngest_age)
        print(name)

def year_finder():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    year = int(input("Wich years Oscar do you want to know?"))
    for i in data:
        if i[1]!="Year":
            if int(i[1]) == year:
                print(i)
year_finder