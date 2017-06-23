import datetime
import csv

if __name__ == '__main__':
    datetime_list = [
        datetime.datetime(2014, 1, 1),
        datetime.datetime(2014, 2, 19),
        datetime.datetime(2014, 3, 13),
        datetime.datetime(2014, 4, 20),
    ]

    datetime_list = map(lambda x: x.strftime("%Y-%m-%d"), datetime_list)

    dates = []

    summe = 0

    with open("dates.csv","r") as f:
        reader = csv.DictReader(f,fieldnames=['date','points'])
        for row in reader:
            dates.append(row['date'])
            summe += float(row['points'])
    print summe
    dates = map(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d"),dates)
    for date in dates:
        print date