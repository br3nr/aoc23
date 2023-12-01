if __name__ == "__main__":
    sum = 0
    with open("input.txt", "r") as file:
        for cell in file:
            nums = []
            for char in cell:
                try:
                    nums.append(int(char))
                except ValueError:
                    pass
            sum = sum + int(str(nums[0]) + str(nums[len(nums) - 1]))
    print(sum)  # Answer is 55538
