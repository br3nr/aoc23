# Star 1

r_m = 12
g_m = 13
b_m = 14
score = 0 

with open("input.txt", "r") as file:
    for line in file:
        valid = True
        clean_line = line.strip().replace(" ", "").replace("Game", "")
        set_id = int(clean_line[:clean_line.rfind(":"):])
        sets = clean_line[clean_line.rfind(":")+1::].split(";")
        
        for subset in sets:
            cubes = subset.split(",")
            r_s = 0
            g_s = 0
            b_s = 0

            for cube in cubes:
                if "red" in cube:
                    r_s = int(cube.replace("red", ""))
                elif "green" in cube:
                    g_s = int(cube.replace("green", ""))

                elif "blue" in cube:
                    b_s = int(cube.replace("blue", ""))
            if r_s > r_m or g_s > g_m or b_s > b_m: 
                valid = False
                break

        if valid:
            score = score + set_id

print(score)
