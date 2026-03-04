
students = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "Diana"}
print(f"Original Dictionary: {students}")


print(f"Access Roll 101: {students[101]}")



print(f"Access Roll 999: {students.get(999, 'Not Found')}")



students[102] = "Robert"
print(f"Updated Roll 102: {students}")



del students[101]
print(f"After 'del' 101: {students}")


removed_student = students.pop(103)
print(f"Popped 103 ({removed_student}): {students}")


count = len(students)
print(f"Number of pairs: {count}")


print(f"Keys:   {list(students.keys())}")
print(f"Values: {list(students.values())}")
print(f"Pairs:  {list(students.items())}")