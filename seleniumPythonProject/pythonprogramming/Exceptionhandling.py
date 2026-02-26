try:

    a = int(input("Enter thr number"))
    b = int(input("Enter thr number"))
    print(a/b)

except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please enter valid numbers")


try:
    a =5//0
except Exception as a:
    print(a)
else:
    print("Division successful")
finally:
    print ("close the browser")


age = int(input ("enter the age"))
if age < 18:
    raise ValueError(" age must be 18 or above")
