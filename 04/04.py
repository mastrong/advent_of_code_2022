with open("input.txt", "r") as f:
    pairs = f.read()

pairs = pairs.split()
fully_contained = 0
overlap = 0

for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_pairs = list(elf1.split("-"))
    elf2_pairs = list(elf2.split("-"))
    elf1 = set(range(int(elf1_pairs[0]), int(elf1_pairs[1]) + 1))
    elf2 = set(range(int(elf2_pairs[0]), int(elf2_pairs[1]) + 1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        fully_contained += 1
    if elf1.intersection(elf2):
        overlap += 1

print(f"Fully contained: {fully_contained}")
print(f"Overlapping: {overlap}")