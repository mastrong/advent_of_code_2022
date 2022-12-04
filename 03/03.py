def get_priority(letter):
    if letter.islower():
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38

    return priority

with open("input.txt", "r") as f:
    sacks = f.read().split()

total = 0

for sack in sacks:
    middle = len(sack) // 2
    comp1 = set(sack[:middle])
    comp2 = set(sack[middle:])
    common = list(comp1.intersection(comp2))
    total += get_priority(common[0])

print(f"Total: {total}")

section = 0
total2 = 0

for i in range(len(sacks)//3):
    chunk = sacks[section:section+3]
    print(chunk)
    common = list(set(chunk[0]).intersection(set(chunk[1])).intersection(set(chunk[2])))
    total2 += get_priority(common[0])
    section += 3

print(f"Total 2: {total2}")
