with open("input.txt", "r") as file:
    lines = file.readlines()
    file_len = len(lines)
    match_map = {key: 1 for key in range(1, file_len + 1)}
    scratch_cards = 0
    for i, line in enumerate(lines):
        scratch_cards += match_map[i + 1]
        winnings_map = {}
        format = line.replace("  ", " ")
        format = format[format.rfind(":") + 1 : :]
        game = format.split("|")

        winnings = game[0].strip().split(" ")
        numbers = game[1].strip().split(" ")

        for winning in winnings:
            winnings_map[winning] = 1

        matches = 0
        for number in numbers:
            if number in winnings_map:
                matches = matches + 1
        if not matches == 0:
            for match in range(matches):
                match_map[match + i + 2] = match_map.get(i + 2 + match, 0) + match_map[i+1]

print(scratch_cards)
