import calendar

year= int(input("Enter year:"))
month=1
while month<13:
    print(calendar.month(year,month))
    month=month+1