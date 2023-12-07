D = open("input.txt").read().strip()
lines = D.split("\n")
hands = []

for line in lines:
    hands.append(line.split(" "))

ranks = [(5,), (1, 4), (2, 3), (1, 1, 3), (1, 2, 2), (1, 1, 1, 2), (1, 1, 1, 1, 1)]
power = "AKQJT98765432"
divisions = {}
winnings, counter = 0, 1

for i, hand in enumerate(hands):
    hand_dict = {}
    for card in hand[0]:
        hand_dict[card] = hand_dict.get(card, 0) + 1
    rank_t = tuple(sorted(hand_dict.values()))
    hand_type = ranks.index((rank_t))
    hand.append(hand_type)

for hand in hands:
    arr = divisions.get(hand[2], [])
    arr.append([hand[0], hand[1]])
    divisions[hand[2]] = arr

for key, division in sorted(divisions.items(), reverse=True):
    if len(division) >= 2:
        sort_division = sorted(
            division, key=lambda rank: [power.index(c) for c in rank[0]], reverse=True
        )
        for hand in sort_division:
            winnings += int(hand[1]) * counter
            counter += 1
    else:
        winnings += int(division[0][1]) * counter
        counter += 1

print(winnings)
