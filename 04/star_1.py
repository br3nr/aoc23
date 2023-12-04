with open("input.txt", "r") as file:
    point_sum = 0
    for line in file:
        format = line.replace("  ", " ")
        format = format[format.rfind(":") + 1 : :]
        game = format.split("|")

        winnings = game[0].strip().split(" ")
        numbers = game[1].strip().split(" ")

        win_nums = [x for x in numbers if x in winnings]
        if len(win_nums):
            point_sum += 2**(len(win_nums)-1)

print(point_sum)
