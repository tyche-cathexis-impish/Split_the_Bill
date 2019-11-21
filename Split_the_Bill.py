bill = int(input("How much?: "))
number_of_people = int(input("How many?: "))

print(f"{bill} yen")
print(f"{number_of_people} nin")
# print({bill}/{number_of_people})
print(f"一人あたり{bill // number_of_people}円です")
print(f"端数は{bill % number_of_people}円です")
