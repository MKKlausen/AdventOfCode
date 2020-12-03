with open(r"C:\Users\skyri\Desktop\AdventOfCode\input_dec3.txt", 'r', encoding='utf-8') as input_file:
    lines = []
    lines = input_file.readlines()
    num_lines = len(lines)
    map = []
    slopes = [(1, 1),(3, 1),(5, 1),(7, 1),(2, 1)]
    tree_counts = []
    for slope in slopes:
        slope_number = 0
        tree_count = 0
        course_x = slope[0]
        course_y = slope[1] 
        for line in lines:
            #repeat for the width.
            i = 0
            line_content = ""
            while i < num_lines:
                line_content = line_content + line.replace("\n", "")
                i = i + 1
            map.append(line_content)
    
        position_x, position_y = 0, 0
        
        while position_y < len(map) and position_x < len(map[0]):
            if map[position_y][position_x] == "#":
                tree_count = tree_count + 1
            position_x = position_x + course_x    
            position_y = position_y + course_y
        tree_counts.append(tree_count)
        print(tree_count)
        slope_number+1
print("TreeCount totals: " + str(tree_counts[1]*tree_counts[2]*tree_counts[3]*tree_counts[4]*tree_counts[0]))