subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print(f"Original: {subjects}")

subjects.sort(key=lambda x: x[1])

print(f"Sorted by Marks: {subjects}")


import datetime
now = datetime.datetime.now()
print(f"Current Date: {now}")

get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day
get_time = lambda x: x.time()

print(f"Year:  {get_year(now)}")
print(f"Month: {get_month(now)}")
print(f"Day:   {get_day(now)}")
print(f"Time:  {get_time(now)}")

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {**dic1, **dic2, **dic3}

print("Concatenated Dictionary:", result)


