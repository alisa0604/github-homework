from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_day = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    for user in users:
        name = user['name']
        birthday = user['birthday']
        if birthday.date() >= start_of_week.date() and birthday.date() <= end_of_week.date():
            weekday = birthday.weekday()
            if weekday == 5 or weekday == 6:
                weekday = 0
            birthdays_per_day[weekday].append(name)

    for i in range(7):
        day = start_of_week + timedelta(days=i)
        day_name = day.strftime('%A')
        names = ", ".join(birthdays_per_day[i])
        if names:
            print(f"{day_name}: {names}")

users = [
    {'name': 'Bill', 'birthday': datetime(2001, 3, 20)},
    {'name': 'Jill', 'birthday': datetime(2000, 3, 27)},
    {'name': 'Kim', 'birthday': datetime(2002, 3, 24)},
    {'name': 'Jan', 'birthday': datetime(2003, 3, 31)},
]

get_birthdays_per_week(users)