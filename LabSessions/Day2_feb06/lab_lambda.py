

nums = [1, 2, 3, 4, 5, 6]



evens = list(filter(lambda x: x % 2 == 0, nums))
print("Step 1 (Filtered Evens):", evens)


squared_numbers = list(map(lambda x: x ** 2, evens))
print("Step 2 (Squared):", squared_numbers)


total_sum = sum(squared_numbers)
print("Step 3 (Final Sum):", total_sum)




salaries = [25000, 40000, 32000, 18000]



high_salaries = list(filter(lambda x: x > 30000, salaries))
print("Step 1 (High Salaries > 30k):", high_salaries)


hiked_salaries = list(map(lambda x: x * 1.10, high_salaries))
print("Step 2 (With 10% Hike):", hiked_salaries)


total_payout = sum(hiked_salaries)
print("Step 3 (Total Payout):", total_payout)


