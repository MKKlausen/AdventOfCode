
with open(r"C:\Users\skyri\Desktop\AdventOfCode\Input\input_dec1.txt", 'r', encoding='utf-8') as input_file:
    numbers = []
    
    for line in input_file.readlines():
        clean_line = line.replace("\n", "")
        numbers.append(clean_line)
valid_combination_part_1 = []
valid_combination_part_2 = []
for first_number in numbers:
    for second_number in numbers:
        if int(first_number) + int(second_number) == 2020:
                valid_combination_part_1.append((first_number, second_number))    
                
        for third_number in numbers:
            if int(first_number) + int(second_number) + int(third_number) == 2020:
                valid_combination_part_2.append((first_number, second_number, third_number))
valid_combination_part_1 = set(tuple(sorted(l)) for l in valid_combination_part_1)
valid_combination_part_2 = set(tuple(sorted(l)) for l in valid_combination_part_2)

result_part_1 = 1
for valid_combo in valid_combination_part_1:
    for number in valid_combo:
        result_part_1 = result_part_1 * int(number)
print("Part 1 solution: " + str(result_part_1))
result_part_2 = 1
for valid_combo in valid_combination_part_2:
    for number in valid_combo:
        result_part_2 = result_part_2 * int(number)
print("Part 2 solution: " + str(result_part_2))

    
