group = [("rahul", 1000),
         ("pankaj" , 700),
         ("divya", 900)]


paid = {}

for name, amount in group:
    if name in paid:
        paid[name] = paid[name] + amount
    else:
        paid[name] = amount

    
total = 0
for amount in paid.values():
    total = total + amount

people = len(paid)
share = total / people

print("Total expense:", total)
print("Each person should pay:", share)
print()

for name, amount in paid.items():
    diff = amount - share

    if diff > 0:
        print(f"{name} should receive {diff}")
    elif diff < 0:
        print(f"{name} should pay {-diff}")
    else:
        print(f"{name} is setteld")
    
