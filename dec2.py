with open(r"C:\Users\skyri\Desktop\input.txt", 'r', encoding='utf-8') as input_file:
    passwords = []
    i = 0  # Rule 1
    k = 0  # Rule 2
    for line in input_file.readlines():
        clean_line = line.replace("\n", "")
        passwords.append(clean_line)

    split_lines = []
    for password in passwords:
        split_lines.append(password.split(" "))

    for line in split_lines:
        least, most = line[0].split("-")
        letter = line[1].split(":")
        if int(most) <= len(line[2]):
            if (letter[0] == line[2][int(least)-1] and letter[0] != line[2][int(most)-1]) or (letter[0] != line[2][int(least)-1] and letter[0] == line[2][int(most)-1]):
                k = k + 1

        count = 0
        for j in line[2]:
            if j == letter[0]:
                count = count + 1
        if int(least) <= count and count <= int(most):
            i = i + 1

print("Rule 1 totals: " + str(i))
print("Rule 2 totals: " + str(k))