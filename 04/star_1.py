with open("input.txt", "r") as file:
    point_sum = 0
    for line in file:
        winnings_map = {}
        format = line.replace("  ", " ")
        format = format[format.rfind(":") + 1 : :]
        game = format.split("|")

        winnings = game[0].strip().split(" ")
        numbers = game[1].strip().split(" ")

        for winning in winnings:
            winnings_map[winning] = 1

        points = 0
        for number in numbers:
            if number in winnings_map:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        point_sum += points

print(point_sum)
