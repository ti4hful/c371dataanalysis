# Cintia Biro-Hajnal 25/10/23

import datetime

def get_time_input():
    try:
        days = int(input("Enter days: "))
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        return days, hours, minutes, seconds
    except ValueError:
        print("Invalid input format. Please enter whole numbers.")
        return get_time_input()

def add_time_duration(time1, time2):
    total_seconds = sum(time1) + sum(time2)
    return total_seconds

def subtract_time_duration(time1, time2):
    total_seconds = sum(time1) - sum(time2)
    return total_seconds

def format_duration(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds

def calculate_date_time(date, time, operation, days, hours, minutes, seconds):
    try:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        time_obj = datetime.datetime.strptime(time, '%H:%M:%S')

        if operation == 'add':
            result_datetime = date_obj + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        elif operation == 'subtract':
            result_datetime = date_obj - datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        else:
            print("Invalid operation. Please choose 'add' or 'subtract'.")
            return None

        result_date = result_datetime.strftime('%Y-%m-%d')
        result_time = result_datetime.strftime('%H:%M:%S')
        return result_date, result_time
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for the date and HH:MM:SS for the time.")
        return None

def calculate_age(start_date, end_date):
    try:
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        age = end_date_obj - start_date_obj
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
        hours, remainder = divmod(age.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return years, months, days, hours, minutes, seconds
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

while True:
    print("Date-Time Calculators")
    print("1. Time Duration Calculator")
    print("2. Add or Subtract Time from a Date")
    print("3. Age Calculator")
    print("4. Exit")

    choice = input("Choose a calculator (1/2/3/4): ")

    if choice == '1':
        print("Time Duration Calculator")
        print("1. Add Time Durations")
        print("2. Subtract Time Durations")
        print("3. Back")
        sub_choice = input("Choose an option (1/2/3): ")

        if sub_choice == '1':
            print("Enter the first time duration:")
            time1 = get_time_input()
            print("Enter the second time duration:")
            time2 = get_time_input()
            result_seconds = add_time_duration(time1, time2)
            days, hours, minutes, seconds = format_duration(result_seconds)
            print(f"Result: {days} days {hours} hours {minutes} minutes {seconds} seconds")
        elif sub_choice == '2':
            print("Enter the first time duration:")
            time1 = get_time_input()
            print("Enter the time duration to subtract:")
            time2 = get_time_input()
            result_seconds = subtract_time_duration(time1, time2)
            days, hours, minutes, seconds = format_duration(result_seconds)
            print(f"Result: {days} days {hours} hours {minutes} minutes {seconds} seconds")
        elif sub_choice == '3':
            continue
        else:
            print("Invalid choice. Please select a valid option.")
    elif choice == '2':
        date = input("Enter a date (YYYY-MM-DD): ")
        time = input("Enter a time (HH:MM:SS): ")
        operation = input("Choose an operation (add/subtract): ")
        days, hours, minutes, seconds = get_time_input()
        result = calculate_date_time(date, time, operation, days, hours, minutes, seconds)
        if result:
            result_date, result_time = result
            print(f"Result: {result_date} {result_time}")
    elif choice == '3':
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        result = calculate_age(start_date, end_date)
        if result:
            years, months, days, hours, minutes, seconds = result
            print(f"Result: {years} years {months} months {days} days {hours} hours {minutes} minutes {seconds} seconds")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
