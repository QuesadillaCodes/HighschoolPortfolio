# From project

def main():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    
    print("Menu:")
    print("1) Calculate the number of days in the given month.")
    print("2) Calculate the number of days passed in the given year.")
    
    option = int(input())
    
    if option == 1:
        days = number_of_days(month, year)
        print(days)
        
    elif option == 2:
        passed_days = days_passed(day, month, year)
        print(passed_days)
    
    else:
        print("Error.")


def leap_year(y):
    if not y % 4 and y % 100:
        return 1
        
    elif not y % 400:
        return 1
    
    return 0


def number_of_days(m, y):
    is_leap_year = leap_year(y)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    
    elif m in [4, 6, 9, 11]:
        return 30
    
    elif m == 2 and is_leap_year:
        return 29
    
    else:
        return 28
    
    
def days_passed(d, m, y):
    sum = 0
    for month in range(1, m):
        sum += number_of_days(month, y)

    return sum + d - 1

main()
