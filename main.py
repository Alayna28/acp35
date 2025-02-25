#using date time project
from datetime import datetime

#store birthdays using datetime objects
birthday1 = datetime(2012, 3, 25)
birthday2 = datetime(2013, 6, 7)
birthday3 = datetime(1987, 4, 7)

#store as string
birthday4 = "1987-07-15"

#store as dictionary
birthday5 = {
    "days" : 30,
    "months" : 12,
    "year" : 2011
}
#print all birthdays to verify
print("Birthday 1:", birthday1)
print("Birthday 2:", birthday2)
print("Birthday 3:", birthday3)
print("Birthday 4:", birthday4)
print("Birthday 5:", birthday5)