numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

number_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "thr3e",
    "four": "fo4r",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}

if __name__ == "__main__":
    sum = 0
    with open("input.txt", "r") as file:
        for cell in file:
            for number in numbers:
                cell = cell.replace(number, str(number_map[number]))
            nums = []
            print(cell)
            for char in cell:
                try:
                    nums.append(int(char))
                except ValueError:
                    pass
            sum = sum + int(str(nums[0]) + str(nums[len(nums) - 1]))
    print(sum)  # Answer is 54875