import csv

with open("mycsv.csv", "w") as cf:
    writer = csv.writer(cf)
    writer.writerow(["id", "name", "familyName", "phone"])
    writer.writerows([
        ["1", "sadegh", "khoshbayan", "021897312"],
        ["2", "ali", "mehdizade", "0218231312"],
        ["3", "abas", "khoshbayan", "021437312"],
        ["4", "mohamad", "sinayi", "02189732312"]
    ]
    )
with open("mycsv.csv") as cf:
    csv_file=csv.reader(cf)
    print(next(csv_file))
    for line in csv_file:
        print(line)