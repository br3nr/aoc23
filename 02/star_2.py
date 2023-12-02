power_sum = 0 

with open("input.txt", "r") as file:
    for line in file:
        r_s = 0
        g_s = 0
        b_s = 0
        clean_line = line.strip().replace(" ", "").replace("Game", "")
        set_id = int(clean_line[:clean_line.rfind(":"):])
        sets = clean_line[clean_line.rfind(":")+1::].split(";")

        for subset in sets:
            cubes = subset.split(",")


            for cube in cubes:
                if "red" in cube:
                    r_temp = int(cube.replace("red", ""))
                    r_s = r_temp if r_temp > r_s else r_s 
                elif "green" in cube:
                    g_temp = int(cube.replace("green", ""))
                    g_s = g_temp if g_temp > g_s else g_s 

                elif "blue" in cube:
                    b_temp = int(cube.replace("blue", ""))
                    b_s = b_temp if b_temp > b_s else b_s 
        
        power_sum = power_sum + (r_s * b_s * g_s)

print(power_sum)
