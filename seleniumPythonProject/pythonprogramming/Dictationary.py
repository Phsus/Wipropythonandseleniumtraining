# dictionary items

country = {
    "India":"Delhi",
    "Canada":"Ottawa",
    "England":"London"
}

print(country)

print(country["Canada"])

country["Italy"] = "Rome"
print(country)

del country["India"]

country.clear()
print(country)

for coun in country:
    print(coun)

my_dict = {1: "one" , 2: "two" , 3: "three"}
print(my_dict)

my_dict = {1: "four" , 2: "two", 3: "three", 1: "one"}
print(my_dict)


my_dict = {(1,2): "one two" , 3:"three"}
print (my_dict)

my_dict = {(1,2): "one two" , 3: "three", 3:"four"}
print(my_dict)



# Initial Dictionary
data = {'a': 1, 'b': 2, 'c': 3}
print(f"Start:    {data}")


print(f"Keys:     {list(data.keys())}")
print(f"Values:   {list(data.values())}")


backup = data.copy()


data.update({'a': 100, 'd': 4})
print(f"Updated:  {data}")


val = data.pop('b')
print(f"Popped 'b': {val}")


item = data.popitem()
print(f"Popitem:  {item}")


print(f"\nFinal:    {data}")
print(f"Backup:   {backup}")


