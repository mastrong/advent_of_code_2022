with open("input.txt", "r") as f:
    calories = f.read()

calories = calories.split("\n")

all_cals = []
current_total = 0

for cal in calories:
    if cal == "":
        all_cals.append(current_total)
        current_total = 0
    else:
        current_total += int(cal)

all_cals.sort(reverse=True)

print(f"Highest calories: {all_cals[0]}.")
print(f"Top 3 calories combined: {sum(all_cals[:3])}")
