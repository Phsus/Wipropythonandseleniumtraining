print("--- 1. ADDING & REMOVING ---")

# add()
s = {1, 2}
s.add(3)
print(f"add(3): {s}")

# remove() - raises error if missing
s = {1, 2, 3}
s.remove(2)
print(f"remove(2): {s}")

# discard() - no error if missing
s = {1, 2, 3}
s.discard(99)
print(f"discard(99) (safe remove): {s}")

# pop() - removes random item
s = {10, 20, 30}
popped = s.pop()
print(f"pop(): {popped} | Remaining: {s}")

# clear()
s = {1, 2, 3}
s.clear()
print(f"clear(): {s}")


print("\n--- 2. SET OPERATIONS (Returns New Set) ---")
a = {1, 2, 3}
b = {3, 4, 5}

# union() |
print(f"union (a | b): {a.union(b)}")

# intersection() &
print(f"intersection (a & b): {a.intersection(b)}")

# difference() -
print(f"difference (a - b): {a.difference(b)}")

# symmetric_difference() ^
print(f"symmetric_difference (a ^ b): {a.symmetric_difference(b)}")

# copy()
c = a.copy()
print(f"copy(): {c}")


print("\n--- 3. UPDATES (Modifies Original Set) ---")
# update()
a = {1, 2}
a.update({3, 4})
print(f"update({3, 4}): {a}")

# difference_update()
a = {1, 2, 3}
a.difference_update({2})
print(f"difference_update({2}): {a}")

# intersection_update()
a = {1, 2, 3}
a.intersection_update({2, 3, 4})
print(f"intersection_update({2, 3, 4}): {a}")

# symmetric_difference_update()
a = {1, 2}
a.symmetric_difference_update({2, 3})
print(f"symmetric_difference_update({2, 3}): {a}")


print("\n--- 4. BOOLEAN CHECKS (True/False) ---")
a = {1, 2}
b = {1, 2, 3}
c = {4, 5}

# isdisjoint() - True if no common elements
print(f"isdisjoint (a vs c): {a.isdisjoint(c)}")

# issubset() <=
print(f"issubset (a <= b): {a.issubset(b)}")

# issuperset() >=
print(f"issuperset (b >= a): {b.issuperset(a)}")